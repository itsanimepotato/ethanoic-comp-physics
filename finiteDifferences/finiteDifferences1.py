Web VPython 3.2

def p(t):
    total = (0.8*t*t*t*t)+(-2.2*t*t*t)+(1.5*t)+1
    return total

pTGraph = graph(title="Position vs. Time", xtitle="Time", ytitle="Position")
pTCurve = gcurve(graph=pTGraph)

tMin = -1
tMax = 2.5

totalTime = tMax - tMin
deltaT = totalTime/67

for t in range(-1,2.5,deltaT):
    pTCurve.plot(t,p(t))

pVGraph = graph(title="Velocity vs. Time", xtitle="Time", ytitle="Velocity")
pVForwardCurve = gcurve(graph=pVGraph, color=color.red, label="Forward Velocity")

def vF(t):
    total = p(t+deltaT) - p(t)
    total = total/deltaT
    return total
    
for t in range(-1,2.5,deltaT):
    pVForwardCurve.plot(t,vF(t))
