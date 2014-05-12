from ent import *
from math import *
import numpy as np
import cairocffi

from PIL import Image, ImageDraw
from PIL import ImageChops

#optional: if you have psyco installed,
#uncomment these lines for a massive speed up!
#import psyco
#psyco.full()

# render a single anti-aliased pixel
def wu_pixel(surf, x, y, value):
    xint = int(floor(x))
    fracx = x - floor(x)
    yint = int(floor(y))
    fracy = y - floor(y)
    btl = (1-fracx)*(1-fracy) * value
    btr = (fracx)*(1-fracy) * value
    bbl = (1-fracx)*(fracy) * value
    bbr = (fracx)*(fracy) * value

    surf[xint,yint] += btl
    surf[xint+1,yint] += btr
    surf[xint,yint+1] += bbl
    surf[xint+1,yint+1] += bbr

#render n points on a res x res grid
def render(res, n):
    #init variables
    pi2 = 2*pi
    half_size = res/2
    basescale = (res/2.2)/ (sqrt(n)+1.0)
    image = np.zeros((res,res), np.float32 )

    for j in range(n):
        i = j + 1

        # compute co-ordinates
        r = sqrt(i)
        theta = r * pi2
        x = cos(theta) * r * basescale + half_size
        y = -sin(theta) * r * basescale + half_size

        if i%10000==0:
            print '%d (%d)' %(i, int(100*i/float(n)))

        #factor
        factors = factor(i)

        if len(factors) > 1:
            strength = pow(2, len(factors)-1)
            wu_pixel(image, x, y, strength)

    #write the image
    mode = "L"
    img = Image.fromstring('RGB', (image.shape[1], image.shape[0]), image.tostring())
    img.show()
    #ImageChops.invert(img).save("spiral.png")


def plot(draw, img, x, y, c, col,steep):
    if steep:
        x,y = y,x
    if x < img.size[0] and y < img.size[1] and x >= 0 and y >= 0:
        c = c * (float(col[3])/255.0)
        p = img.getpixel((x,y))
        draw.point((int(x),int(y)),fill=(int((p[0]*(1-c)) + col[0]*c), int((p[1]*(1-c)) + col[1]*c), int((p[2]*(1-c)) + col[2]*c),255))

def iround(x):
    return ipart(x + 0.5)

def ipart(x):
    return math.floor(x)

def fpart(x):
    return x-math.floor(x)

def rfpart(x):
    return 1 - fpart(x)


def drawLine(draw, img, x1, y1, x2, y2, col):
    dx = x2 - x1
    dy = y2 - y1

    steep = abs(dx) < abs(dy)
    if steep:
        x1,y1=y1,x1
        x2,y2=y2,x2
        dx,dy=dy,dx
    if x2 < x1:
        x1,x2=x2,x1
        y1,y2=y2,y1
    gradient = float(dy) / float(dx)

    #handle first endpoint
    xend = round(x1)
    yend = y1 + gradient * (xend - x1)
    xgap = rfpart(x1 + 0.5)
    xpxl1 = xend    # this will be used in the main loop
    ypxl1 = ipart(yend)
    plot(draw, img, xpxl1, ypxl1, rfpart(yend) * xgap,col, steep)
    plot(draw, img, xpxl1, ypxl1 + 1, fpart(yend) * xgap,col, steep)
    intery = yend + gradient # first y-intersection for the main loop

    #handle second endpoint
    xend = round(x2)
    yend = y2 + gradient * (xend - x2)
    xgap = fpart(x2 + 0.5)
    xpxl2 = xend    # this will be used in the main loop
    ypxl2 = ipart (yend)
    plot (draw, img, xpxl2, ypxl2, rfpart (yend) * xgap,col, steep)
    plot (draw, img, xpxl2, ypxl2 + 1, fpart (yend) * xgap,col, steep)

    #main loop
    for x in range(int(xpxl1 + 1), int(xpxl2 )):
        plot(draw, img, x, ipart(intery), rfpart (intery),col, steep)
        plot(draw, img, x, ipart(intery) + 1, fpart (intery),col, steep)
        intery += gradient

def render2(res, n):
    #init variables
    pi2 = 2 * pi
    half_size = res/2
    basescale = (res/2.2) / (sqrt(n) + 1.0)
    image = np.zeros((res, res), np.float32)

    for j in range(n):
        i = j + 1
        # compute co-ordinates
        r = sqrt(i)
        theta = r * pi2
        x = cos(theta) * r * basescale + half_size
        y = -sin(theta) * r * basescale + half_size
        if i % 10000 == 0:
            print('%d (%d)' % (i, int(100*i/float(n))))
        #factor
        factors = factor(i)
        if len(factors) > 1:
            strength = pow(2, len(factors)-1)
            wu_pixel(image, x, y, strength)

    #write the image
    img = Image.fromstring('RGB', (image.shape[1], image.shape[0]), image.tostring())
    img.show()
    #ImageChops.invert(img).save("spiral.png")

img = Image.new('RGBA', (200, 300), (0, 0, 255, 255))
draw = ImageDraw.Draw(img)
#draw.line((100, 100, 200, 200))
#drawLine(draw, img, 100, 100, 200, 200, (50, 50, 255, 50))
# draw cross on top of PIL image


surface = cairocffi.ImageSurface(cairocffi.FORMAT_RGB24, 300, 200)
context = cairocffi.Context(surface)
with context:
    context.set_source_rgb(1, 1, 1)  # White
    context.paint()

# Restore the default source which is black.
linear = cairocffi.LinearGradient(0, 0, 1, 1)
linear.add_color_stop_rgb(0, 0, 0.3, 0.8)
linear.add_color_stop_rgb(1, 0, 0.8, 0.3)

radial = cairocffi.RadialGradient(0.5, 0.5, 0.25, 0.5, 0.5, 0.75)
radial.add_color_stop_rgba(0, 0, 0, 0, 1)
radial.add_color_stop_rgba(0.5, 0, 0, 0, 0)



context.set_line_width(10)
context.set_source_rgb(0, 0, 0)
context.rectangle(0, 0, 10, 20)
context.stroke()
surface.write_to_png('example.png')

#render2(res=4096,n = 1000)