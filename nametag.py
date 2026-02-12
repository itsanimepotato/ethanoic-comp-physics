Web VPython 3.2
import random

print("this was made using boxes, spheres, arrows, helixes, and curves")


def rc():
    randNum = random.randint(0,7)
    if randNum == 0:
        return color.white
    elif randNum == 1:
        return color.red
    elif randNum == 2:
        return color.green
    elif randNum == 3:
        return color.blue
    elif randNum == 4:
        return color.cyan
    elif randNum == 5:
        return color.magenta
    else randNum == 6:
        return color.yellow

thick = 0.5
height = 4
space = 2
gap = 3

def E(pos):
    box(pos=pos+vector(-space/2,0,0), size=vector(thick,height,thick), color=rc())
    box(pos=pos+vector(0,height/2,0), size=vector(space,thick,thick), color=rc())
    box(pos=pos, size=vector(space,thick,thick), color=rc())
    box(pos=pos+vector(0,-height/2,0), size=vector(space,thick,thick), color=rc())

def T(pos):
    box(pos=pos+vector(0,height/2,0), size=vector(space,thick,thick), color=rc())
    sphere(pos=pos+vector(0,height/2,0)+vector(space-2,thick-1,thick), color=rc(), radius=thick)
    sphere(pos=pos+vector(0,height/2,0)+vector(space-2,thick-2,thick), color=rc(), radius=thick)
    sphere(pos=pos+vector(0,height/2,0)+vector(space-2,thick-3,thick), color=rc(), radius=thick)
    sphere(pos=pos+vector(0,height/2,0)+vector(space-2,thick-4,thick), color=rc(), radius=thick)
    sphere(pos=pos+vector(0,height/2,0)+vector(space-2,thick-5,thick), color=rc(), radius=thick)

def H(pos):
    box(pos=pos+vector(-space/2,0,0), size=vector(thick,height,thick), color=rc())
    box(pos=pos+vector(space/2,0,0), size=vector(thick,height,thick), color=rc())
    box(pos=pos, size=vector(space,thick,thick), color=rc())

def A(pos):
    arrow(pos=pos+vector(-space/2,-height/2,0),
          axis=vector(space/2,height,0),
          shaftspace=thick,
          color=rc())
    arrow(pos=pos+vector(space/2,-height/2,0),
          axis=vector(-space/2,height,0),
          shaftspace=thick,
          color=rc())
    box(pos=pos+vector(space/5,-height/10,0),
        size=vector(space,thick,thick),
        color=rc())

def N(pos):
    box(pos=pos+vector(-space/2,0,0), size=vector(thick,height,thick), color=rc())
    box(pos=pos+vector(space/2,0,0), size=vector(thick,height,thick), color=rc())
    arrow(pos=pos+vector(-space/2,height/2,0),
          axis=vector(space,-height,0),
          shaftspace=thick,
          color=rc())

def C(pos):
    helix(pos=pos, axis=vector(0,0,1), radius=2, thickness=thick, coils=0.25, color=rc())

    R = 5
    arc = curve(color=rc(), radius=thick/2)
    arc.append(pos=vector(pos.x-2,0,0))
    for theta in range(180, 270):
        rad = theta * pi / 180
        arc.append(pos=vector(R*cos(rad)+pos.x+3, R*sin(rad), 0))

# ----- DRAW NAME -----
letters = [E, T, H, A, N, C]
x = -10

for L in letters:
    L(vector(x,0,0))
    x += space + gap
