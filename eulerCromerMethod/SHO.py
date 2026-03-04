Web VPython 3.2

velVsPosGraph = graph(title="Velocity vs. Position", xtitle="Position", ytitle="Velocity")
velVsPosCurve = gcurve(graph=velVsPosGraph)



#####    SET UP OBJECTS   ############

scene.userzoom = False
wall = box(pos=vector(-3, 0, 0), height = 3, length=0.1, texture=textures.wood)
ball = sphere(pos=vector(4,0,0), radius=0.3, color=color.yellow)
spring = helix(pos=wall.pos, axis=(ball.pos-wall.pos), coils=20, radius=0.2)

#####     ADDING NON-NATIVE ATTRIBUTES TO THE BALL AND SPRING   #######


ball.vel = vector(0,0,0)     # Looks the same
ball.acc = vector(0,0,0)     # This is competely unnecessary
ball.mass = 10               # Ball moves slower when mass increases

equilPos = vector(2,0,0)      # I chose this at random
spring.k = 200               # Ball moves quicker when spring constant increases

ball.pos = vector(4,0,0) # Ball starts closer to the wall
#####    MAKING A SPRING FORCE  #############

def springForce(displacement):
    return -spring.k*(displacement-equilPos)


#####    SETTING UP A TIME FRAMEWORK  #########

t = 0
dt = 0.01                    # Time step = 10 milliseconds



#####   MAXIMA  #####
velSign = sign(ball.vel.x)
prevTime = 0

def maxima(t):
    global velSign
    global t
    global prevTime
    diffTime = t-prevTime
    
    if velSign != sign(ball.vel.x):
        print("extrema at " + t)
        print("amt of time between extrema: " + diffTime)
        prevTime = t
    velSign = sign(ball.vel.x)

while True:
    rate(100)               # This runs the loop in pseudo-real time.
    t += dt
# Find the current acceleration here
    ball.acc = springForce(ball.pos)/ball.mass
# Update the velocity of the ball here
    ball.vel += ball.acc*dt
# Update the position of the ball here
    ball.pos += ball.vel*dt
# Spring looks weird? Fix it here
    spring.axis = ball.pos-wall.pos
    maxima(t)
    
# V vs X graph
    velVsPosCurve.plot(ball.pos.x,ball.vel.x)
    





# SCENARIO, amplitude, period
# M inc, no effect, increase
# K inc, no effect, decrease
# A inc, decrease, no effect?
# V inc, increase, no effect?
