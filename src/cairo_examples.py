import cairocffi
import math

width = 300
height = 200
surface = cairocffi.ImageSurface(cairocffi.FORMAT_RGB24, width, height)
context = cairocffi.Context(surface)
with context:
    context.set_source_rgb(1, 1, 1)  # White
    context.paint()

context.set_line_width(9)
context.set_source_rgb(0.7, 0.2, 0.0)
context.translate(width / 2, height / 2)
context.arc(0, 0, 50, 0, 2*math.pi)
context.stroke_preserve()
context.set_source_rgb(0.3, 0.4, 0.6)
context.fill()
# Restore the default source which is black.
linear = cairocffi.LinearGradient(0, 0, 1, 1)
linear.add_color_stop_rgb(0, 0, 0.3, 0.8)
linear.add_color_stop_rgb(1, 0, 0.8, 0.3)

radial = cairocffi.RadialGradient(0.5, 0.5, 0.25, 0.5, 0.5, 0.75)
radial.add_color_stop_rgba(0, 0, 0, 0, 1)
radial.add_color_stop_rgba(0.5, 0, 0, 0, 0)

context.set_line_width(10)
context.move_to(0, 0)
context.set_source_rgb(0, 0, 0)
context.rectangle(0, 0, 10, 20)
context.stroke()
surface.write_to_png('example.png')