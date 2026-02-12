Web VPython 3.2

def hypCos(a):
    add = exp(a) + exp(-a)
    return add/2

trigCanvas = graph(title="catenary", xtitle="x", ytitle="y")

trigCurve = gcurve(graph=trigCanvas, color=color.red, label="y=(e^a + e^-a)/2")

for t in range(-5,5,0.01):
    trigCurve.plot(t,hypCos(t))
