Web VPython 3.2

mols = 20
rad = 1
space = 2

lattice = []
Na = sphere(pos=vector(0,0,0),color=color.orange,radius=rad)
Cl = sphere(pos=vector(0,0,0),color=color.green,radius=rad)



for x in range(mols):
    for y in range(mols):
        for z in range(mols):

            tempPos = vector(x*rad*space, y*rad*space, z*rad*space)
            if (x+y+z)%2 == 0:
                atom = sphere(pos=tempPos,radius=rad,color=color.orange)
                lattice.append(atom)
            else:
                atom = sphere(pos=tempPos,radius=rad*1.5,color=color.green)
                lattice.append(atom)
