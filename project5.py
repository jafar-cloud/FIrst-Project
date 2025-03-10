from math import sin, cos, tan, radians, degrees
import matplotlib.pyplot as mplp

angles = [(i) for i in range(360)]
sin_vals = [sin((i)) for i in range(360)]
cos_vals = [cos((i)) for i in range(360)]
tan_vals = [tan((i)) for i in range(360)]

mplp.plot(angles, sin_vals, color="blue", label='Sin')
mplp.plot(angles, cos_vals, color="red", label='Cos')
mplp.plot(angles, tan_vals, color="green", label='Tan')
mplp.show()