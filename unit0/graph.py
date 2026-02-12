Web VPython 3.2

def decayingSine(X):
    return sin(3*X)*exp(-2*X)

trigCanvas = graph(title="deecayihnng sighn kurve", xtitle="thyme")

trigCurve = gcurve(graph=trigCanvas, color=color.red, label="y=sin(3t)*-2^t")

for t in range(0,12,0.01):
    trigCurve.plot(t,decayingSine(t))
