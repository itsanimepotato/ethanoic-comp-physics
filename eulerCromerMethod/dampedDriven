Web VPython 3.2


scene.userzoom = False
wall = box(pos=vector(-3, 0, 0), height = 3, length=0.1, texture=textures.wood)
ball = sphere(pos=vector(4,0,0), radius=0.3, color=color.yellow)
spring = helix(pos=wall.pos, axis=(ball.pos-wall.pos), coils=20, radius=0.2)


ball.vel = vector(0,0,0)   
ball.acc = vector(0,0,0)    
ball.mass = 10              

equilPos = vector(2,0,0)  
spring.k = 200             

ball.pos = vector(4,0,0) 

t = 0
dt = 0.01  

velSign = sign(ball.vel.x)
prevTime = 0

ptGraph = graph(title="Position vs Time", xtitle="Time", ytitle="Position")
ptDots = gdots(graph=ptGraph)
vpGraph = graph(title="Velocity vs Position", xtitle="Position", ytitle="Velocity")
vpDots = gdots(graph=vpGraph)

def springForce(displacement):
    return -spring.k*(displacement-equilPos)

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

def damping(t):
    #dampingForce = 2.5*sqrt(ball.mass*spring.k)
    dampingForce = sqrt(spring.k/ball.mass)*0.2
    return dampingForce

while True:
    rate(100)              
    t += dt   
    ball.acc = springForce(ball.pos)/ball.mass
    ball.acc.x -= ball.vel.x*damping()
    ball.vel += ball.acc*dt
    ball.pos += ball.vel*dt
    spring.axis = ball.pos-wall.pos
    maxima(t)
    
    ptDots.plot(t,ball.pos.x)
    vpDots.plot(ball.pos.x,ball.vel.x)
