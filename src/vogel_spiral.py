from pyx import *
from ent import *
from math import *

#n = 100000
n = 1000
ca = canvas.canvas()

phi = (1 + sqrt(5)) / 2.0

def hexagon():
    ca.stroke(path.line(0, 0, 0, -1))
    ca.stroke(path.line(0, -1, 1, -1))
    ca.stroke(path.line(1, -1, 2, 0))
    ca.stroke(path.line(2, 0, 2, 1))
    ca.stroke(path.line(2, 1, 1, 1))
    ca.stroke(path.line(1, 1, 0, 0))

for j in range(n):
    i = j + 1
    r = sqrt(i)
    theta = i * 2 * pi / (phi*phi)
    x = cos(theta) * r
    y = sin(theta) * r
    if i <= n:
        factors = factor(i)
        n_fac = 0
        for f in factors:
            n_fac += f[1]

        if n_fac > 1:
            print n_fac
            radius = 0.05 * pow(2, (n_fac + 3)/2.5)
            p = path.line(x, y, x, y-1) << path.line(x, y-1, x+1, y-1) << path.line(x+1, y-1, x+2, y) << path.line(x+2, y, x+2, y+1) << path.line(x+2, y+1, x+1, y+1) << path.line(x+1, y+1, x, y)
            p.append(path.closepath())
            ca.fill(p)
            #ca.fill(path.circle(x, y, radius))


d = document.document(pages = [document.page(ca, paperformat=document.paperformat.A4, fittosize=1)])
d.writePSfile("spiral_vogel_all.ps")