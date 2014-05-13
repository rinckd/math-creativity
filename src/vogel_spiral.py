from pyx import *
from ent import *
from math import *

#n = 100000
n = 1000
ca = canvas.canvas()

phi = (1 + sqrt(5)) / 2.0

def hexagon():
    ca.stroke(path.line(-1, 0, 0, -1))
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

            ca.stroke(p.path(), [style.linewidth.Thick, color.rgb.black])
            #ca.fill(p, [color.lineargradient(color.gradient.rgb(0, 0, 0), color.gradient.rgb(1, 1, 1))])
            if n_fac == 1:
                ca.fill(p,  [color.cmyk(25.0/100.0, 0.0/100.0, 0.0/100.0, 0)])
            elif n_fac == 2:
                ca.fill(p,  [color.cmyk(57.0/100.0, 17.0/100.0, 14.0/100.0, 0)])
            elif n_fac == 3:
                ca.fill(p,  [color.cmyk(66.0/100.0, 22.0/100.0, 14.0/100.0, 0)])
            elif n_fac == 4:
                ca.fill(p,  [color.cmyk(78.0/100.0, 30.0/100.0, 14.0/100.0, 0)])
            elif n_fac == 5:
                ca.fill(p,  [color.cmyk(83.0/100.0, 41.0/100.0, 14.0/100.0, 0)])
            elif n_fac == 6:
                ca.fill(p,  [color.cmyk(84.0/100.0, 41.0/100.0, 15.0/100.0, 0.0/100.0)])
            elif n_fac == 7:
                ca.fill(p,  [color.cmyk(89.0/100.0, 54.0/100.0, 6.0/100.0, 0.0/100.0)])
            elif n_fac == 8:
                ca.fill(p,  [color.cmyk(97.0/100.0, 82.0/100.0, 1.0/100.0, 0.0/100.0)])
            elif n_fac == 9:
                ca.fill(p,  [color.cmyk(100.0/100.0, 88.0/100.0, 0.0/100.0, 0.0/100.0)])
            elif n_fac == 10:
                ca.fill(p,  [color.cmyk(100.0/100.0, 90.0/100.0, 0.0/100.0, 0.0/100.0)])
            elif n_fac == 11:
                ca.fill(p,  [color.cmyk(100.0/100.0, 92.0/100.0, 0.0/100.0, 0.0/100.0)])
            elif n_fac == 12:
                ca.fill(p,  [color.cmyk(100.0/100.0, 100.0/100.0, 0.0/100.0, 0.0/100.0)])

            #ca.fill(p, [color.gray(0.8)])
            #ca.fill(path.circle(x, y, radius))


d = document.document(pages=[document.page(ca, paperformat=document.paperformat.A4, fittosize=1)])
d.writePDFfile("spiral_vogel_all.pdf")
d.writePSfile("spiral_vogel_all.ps")