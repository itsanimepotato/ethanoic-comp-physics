Web VPython 3.2

a = float(input("what you have"))
b = float(input("what you want"))

print("the sum of",a,"and",b,"is what you have and want which is",a+b)

while True:
    rate(5)
    theBox = box()
    randBox()
    outputStuff()
    a = infAdd(a,b)
    b = infAdd(a,b)

    print("the surface area of the new block is like: "+ surfArea(theBox))



def randBox():
    theBox.pos = vector.random()
    theBox.color = vector.random()
    theBox.size = vector.random()

def outputStuff():
    print("hiiiii")
    print(theBox.color)
    print("the box volume is ", theBox.length*theBox.height*theBox.width)

def infAdd(a,b):
    print(a+b)
    return(a+b)

def surfArea(block):
    return(abs(block.length*block.height*2+block.length*block.width*2+block.height*block.width*2))
    
