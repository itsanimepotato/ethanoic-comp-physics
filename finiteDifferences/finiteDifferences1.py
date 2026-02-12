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

pVTrueCurve = gcurve(graph=pVGraph, color=color.black, label="True Velocity")

def v(t):
    total = (3.2*t*t*t)+(-6.6*t*t)+1.5
    return total

for t in range(-1,2.5,deltaT):
    pVTrueCurve.plot(t,v(t))

pVForwardCurve = gcurve(graph=pVGraph, color=color.red, label="Forward Velocity")

def vF(t):
    total = p(t+deltaT) - p(t)
    total = total/deltaT
    return total

for t in range(-1,2.5,deltaT):
    pVForwardCurve.plot(t,vF(t))

pVBackwardCurve = gcurve(graph=pVGraph, color=color.green, label="Backward Velocity")

def vB(t):
    total = p(t) - p(t-deltaT)
    total = total/deltaT
    return total

for t in range(-1,2.5,deltaT):
    pVBackwardCurve.plot(t,vB(t))

pVCentralCurve = gcurve(graph=pVGraph, color=color.blue, label="Central Velocity")

def vC(t):
    total = p(t+deltaT) - p(t-deltaT)
    total = total/(deltaT*2)
    return total

for t in range(-1,2.5,deltaT):
    pVCentralCurve.plot(t,vC(t))
