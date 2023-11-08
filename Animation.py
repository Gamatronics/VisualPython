import vpython as vp
import numpy as np

""" piston_1=vp.cylinder(radius=1,
                    lenght=3,
                    color=vp.color.red,
                    opacity=0.25) """
sphere_1 = vp.sphere(radius=1, color=vp.color.red, opacity=0.5)

while True:
    for my_opacity in np.linspace(0.1, 1, 1000):
        vp.rate(250)
        sphere_1.radius = my_opacity
    for my_opacity in np.linspace(1, 0.1, 1000):
        vp.rate(250)
        sphere_1.radius = my_opacity
