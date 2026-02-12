Web VPython 3.2


body = box()

body.color = color.red
body.height = 2

glasses = ellipsoid()

glasses.color = color.cyan
glasses.pos = vector(0.5,0.5,0)
glasses.size = vector(0.75,0.75,0.75)

def antenna(dx,dz):
    antenna = helix()
    antenna.pos = vector(dx,1,dz)
    antenna.axis = vector.random()
    antenna.radius = 0.25
    antenna.color = vector.random()
    antenna.length = 10

antenna(1,1)
antenna(-1,-1)

def leg(dx,dz):
    leg = box()
    leg.pos = vector(dx,-1,dz)
    leg.axis = vector(0,-1,0)
    leg.color = vector.random()

    
leg(.5,.5)
leg(-.5,-.5)
