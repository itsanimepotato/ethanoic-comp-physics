Web VPython 3.2

scene.userzoom = False

wall = box(pos=vector(-3, 0, 0), height=3, length=0.1, texture=textures.wood)
ball = sphere(pos=vector(4,0,0), radius=0.3, color=color.yellow)
spring = helix(pos=wall.pos, axis=(ball.pos-wall.pos), coils=20, radius=0.2)

ball.vel = vector(0,0,0)
ball.acc = vector(0,0,0)
ball.mass = 10
equilPos = vector(2,0,0)
spring.k = 200

t = 0
dt = 0.001

prevVel = 0
prevTime = 0
periodMeasured = False

def detectPeriod():
    global prevVel, prevTime, t
    
    if prevVel > 0 and ball.vel.x <= 0:
        if prevTime != 0:
            T = t - prevTime
            if not pdStop:
                print("Measured Period =", T)
            pdStop = False
        prevTime = t
        
    prevVel = ball.vel.x

def setInitialPosition(s):
    if paused:
        ball.pos = vector(s.value, 0, 0)
        ball.vel = vector(0,0,0)
        spring.axis = ball.pos - wall.pos
        initialPosText.text = "Initial Position = {:1.2f}".format(s.value)

scene.append_to_caption("\n\nAdjust Initial Position Before Starting\n")
initialPosText = wtext(text="Initial Position = 4.00\n")

posSlider = slider(min=1, max=6, value=4, length=300, bind=setInitialPosition)

paused = True

def pause(b):
    global paused
    paused = not paused
    
    if paused:
        b.text = "Start Simulation"
        posSlider.disabled = False
    else:
        b.text = "Stop Simulation"
        posSlider.disabled = True
        pdStop = True

scene.append_to_caption("\n\n")
startButton = button(text="Start Simulation", bind=pause)

def springForce(displacement):
    return -spring.k * (displacement - equilPos)

while True:
    rate(1000)
    
    if not paused:
        t += dt
        
        ball.acc = springForce(ball.pos)/ball.mass
        ball.vel.x += ball.acc.x * dt
        ball.pos += ball.vel * dt
        
        spring.axis = ball.pos - wall.pos
        
        detectPeriod()
