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
            radius = 0.1 * pow(2, (n_fac)/2.5)
            ca.stroke(path.circle(x, y, radius), [style.linewidth.Thick, color.rgb.black])

            #ca.fill(p, [color.lineargradient(color.gradient.rgb(0, 0, 0), color.gradient.rgb(1, 1, 1))])
            if n_fac == 1:
                ca.fill(path.circle(x, y, radius),  [color.rgb(255.0/255.0, 247.0/255.0, 251.0/255.0)])
            elif n_fac == 2:
                ca.fill(path.circle(x, y, radius),  [color.rgb(236.0/255.0, 231.0/255.0, 242.0/255.0)])
            elif n_fac == 3:
                ca.fill(path.circle(x, y, radius),  [color.rgb(208.0/255.0, 209.0/255.0, 230.0/255.0)])
            elif n_fac == 4:
                ca.fill(path.circle(x, y, radius),  [color.rgb(166.0/255.0, 189.0/255.0, 219.0/255.0)])
            elif n_fac == 5:
                ca.fill(path.circle(x, y, radius),  [color.rgb(116.0/255.0, 169.0/255.0, 207.0/255.0)])
            elif n_fac == 6:
                ca.fill(path.circle(x, y, radius),  [color.rgb(54.0/255.0, 144.0/255.0, 192.0/255.0)])
            elif n_fac == 7:
                ca.fill(path.circle(x, y, radius),  [color.rgb(5.0/255.0, 112.0/255.0, 176.0/255.0)])
            elif n_fac == 8:
                ca.fill(path.circle(x, y, radius),  [color.rgb(4.0/255.0, 90.0/255.0, 141.0/255.0)])
            elif n_fac == 9:
                ca.fill(path.circle(x, y, radius),  [color.rgb(2.0/255.0, 56.0/255.0, 88.0/255.0)])
            elif n_fac == 10:
                ca.fill(path.circle(x, y, radius),  [color.rgb(2.0/255.0, 56.0/255.0, 88.0/255.0)])
            elif n_fac == 11:
                ca.fill(path.circle(x, y, radius),  [color.rgb(2.0/255.0, 56.0/255.0, 88.0/255.0)])
            elif n_fac == 12:
                ca.fill(path.circle(x, y, radius),  [color.rgb(2.0/255.0, 56.0/255.0, 88.0/255.0)])

            #ca.fill(p, [color.gray(0.8)])
            #ca.fill(path.circle(x, y, radius))


d = document.document(pages=[document.page(ca, paperformat=document.paperformat.A4, fittosize=1)])
d.writePDFfile("spiral_vogel_all.pdf")
d.writePSfile("spiral_vogel_all.ps")