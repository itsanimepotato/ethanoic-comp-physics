Web VPython 3.2
myList = []
print(myList)

myList.append(67)
print(myList)

for i in range(0,1000,45):
    print(i)
    myList.append(i)
print(myList)


spheres = []

for i in range(10):
    spheres.append(sphere(pos=vector(i*2,0,0), color=vector(0,i,i), emissive=True,shininess=1))

t=0
dt=0.1

while(True):
    rate(100)
    t += dt
    for i in range(10):
        spheres[i].pos.y = sin(i+t)

print(spheres)
