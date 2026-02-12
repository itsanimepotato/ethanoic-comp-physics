Web VPython 3.2

lineCanvas = graph(title='linearish', xtitle='x', ytitle='y', xmin=0, ymin=0)

lineDots = gdots()

def linearish(a):
    valY = a/2
    return valY + random(-100,100)

for i in range(0,10,0.1):
    lineDots.plot(i,linearish(i))
