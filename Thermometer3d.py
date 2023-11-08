import vpython as vp
import numpy as np

glass_bulb_1 = vp.sphere(radius=1.25, color=vp.color.white, opacity=0.3)
glass_cyilinder_1 = vp.cylinder(
    radius=0.65, length=6, color=vp.color.white, opacity=0.3
)
mercury_1 = vp.sphere(radius=1, color=vp.color.red, opacity=1)
mercury_cyilinder_1 = vp.cylinder(radius=0.45, length=6, color=vp.color.red, opacity=1)

thermometer_offset = -5
glass_bulb_2 = vp.sphere(
    radius=1.25,
    color=vp.color.white,
    opacity=0.3,
    pos=vp.vector(0, thermometer_offset, 0),
)
glass_cyilinder_2 = vp.cylinder(
    radius=0.65,
    length=6,
    color=vp.color.white,
    opacity=0.3,
    pos=vp.vector(0, thermometer_offset, 0),
)
mercury_2 = vp.sphere(
    radius=1, color=vp.color.red, opacity=1, pos=vp.vector(0, thermometer_offset, 0)
)
mercury_cyilinder_2 = vp.cylinder(
    radius=0.45,
    length=6,
    color=vp.color.red,
    opacity=1,
    pos=vp.vector(0, thermometer_offset, 0),
)


for tick in np.linspace(1, 6, 15):
    vp.box(
        size=vp.vector(0.05, 0.5, 0.25),
        pos=vp.vector(tick, 0, 0.5),
        color=vp.color.white,
    )
    vp.box(
        size=vp.vector(0.05, 0.5, 0.25),
        pos=vp.vector(tick, thermometer_offset, 0.5),
        color=vp.color.white,
    )

rate = 25
thermometer_1_length = 1
thermometer_2_length = 1
thermometer_1_speed = 6 / 100
thermometer_2_speed = 2 * thermometer_1_speed

while True:
    vp.rate(rate)
    thermometer_1_length += thermometer_1_speed
    thermometer_2_length += thermometer_2_speed

    if thermometer_1_length >= 6 or thermometer_1_length <= 1:
        thermometer_1_speed = -thermometer_1_speed
    if thermometer_2_length >= 6 or thermometer_2_length <= 1:
        thermometer_2_speed = -thermometer_2_speed

    mercury_cyilinder_1.length = thermometer_1_length
    mercury_cyilinder_2.length = thermometer_2_length
