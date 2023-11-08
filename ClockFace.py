import vpython as vp
import numpy as np
import time as tm

clock_radius = 1
ticks_pos = clock_radius - 0.15
major_ticks_size = (0.15, 0.016, 0.01)

clock_face = vp.cylinder(length=0.01, radius=clock_radius, axis=vp.vector(0, 0, 1))

for major_ticks in range(0, 360, 30):
    # print(major_ticks)
    vp.box(
        pos=vp.vector(
            ticks_pos * np.sin(np.deg2rad(major_ticks)),
            ticks_pos * np.cos(np.deg2rad(major_ticks)),
            0.01,
        ),
        size=vp.vector(0.15, 0.018, 0.01),
        color=vp.color.black,
        axis=vp.vector(
            ticks_pos * np.sin(np.deg2rad(major_ticks)),
            ticks_pos * np.cos(np.deg2rad(major_ticks)),
            0,
        ),
    )

numbers = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]

""" for number in numbers:
    #print(major_ticks)
    vp.text(pos = vp.vector(ticks_pos*np.sin(np.deg2rad(major_ticks)),ticks_pos*np.cos(np.deg2rad(major_ticks)),0.01),
           size = vp.vector(0.15,0.018,0.01),
           color = vp.color.black,
           axis = vp.vector(ticks_pos*np.sin(np.deg2rad(major_ticks)),ticks_pos*np.cos(np.deg2rad(major_ticks)),0))
 """

number_height = clock_radius / 6
number_pos = clock_radius * 0.62


number_angle = 90 - 30
angle_inc = -30
for i in range(1, 13):
    clock_numbers = vp.text(
        text=str(i),
        align="center",
        color=vp.color.orange,
        height=number_height,
        pos=vp.vector(
            number_pos * np.cos(np.deg2rad(number_angle)),
            number_pos * np.sin(np.deg2rad(number_angle)) - number_height / 2,
            0,
        ),
        depth=0.1,
    )
    number_angle += angle_inc

""" clock_numbers = vp.text(text = "12",
                            align = "center",
                            color = vp.color.orange,
                            height = number_height,
                            pos = vp.vector(number_pos*np.cos(np.deg2rad(0)),number_pos*np.sin(np.deg2rad(00)),0),
                            depth = 0.1) """

for minor_ticks in range(0, 360, 6):
    # print(major_ticks)
    if not (minor_ticks % 30 == 0):
        vp.box(
            pos=vp.vector(
                ticks_pos * np.sin(np.deg2rad(minor_ticks)),
                ticks_pos * np.cos(np.deg2rad(minor_ticks)),
                0.01,
            ),
            size=vp.vector(0.10, 0.007, 0.01),
            color=vp.color.black,
            axis=vp.vector(
                ticks_pos * np.sin(np.deg2rad(minor_ticks)),
                ticks_pos * np.cos(np.deg2rad(minor_ticks)),
                0,
            ),
        )

arrow_length = clock_radius * 0.75
arrow_thick = 0.02
theta_minutes = 90
theta_hours = 0

hour_arrow_length = arrow_length * 0.60
hour_arrow_tick = arrow_thick

joint = vp.sphere(
    radius=arrow_length / 20, color=vp.color.black, pos=vp.vector(0, 0, 0.02)
)

second_arrow = vp.arrow(
    color=vp.color.red,
    length=clock_radius,
    shaftwidth=arrow_thick / 5,
    axis=vp.vector(
        clock_radius * np.cos(np.deg2rad(theta_minutes)),
        clock_radius * np.sin(np.deg2rad(theta_minutes)),
        0.01,
    ),
    pos=vp.vector(0, 0, 0.02),
    headwidth=0.001,
)

minute_arrow = vp.arrow(
    color=vp.color.black,
    length=arrow_length,
    shaftwidth=arrow_thick,
    axis=vp.vector(
        arrow_length * np.cos(np.deg2rad(theta_minutes)),
        arrow_length * np.sin(np.deg2rad(theta_minutes)),
        0.01,
    ),
    pos=vp.vector(0, 0, 0.02),
)

hour_arrow = vp.arrow(
    color=vp.color.black,
    length=hour_arrow_length,
    shaftwidth=hour_arrow_tick,
    axis=vp.vector(
        hour_arrow_length * np.cos(np.deg2rad(theta_hours)),
        hour_arrow_length * np.sin(np.deg2rad(theta_hours)),
        0.01,
    ),
    pos=vp.vector(0, 0, 0.02),
)
theta = 90
theta_delta = -6
theta_hour = theta - 90
theta_seconds = theta

text_height = clock_radius / 4

my_label = vp.text(
    text="Texas Time",
    align="center",
    color=vp.color.orange,
    height=text_height,
    pos=vp.vector(0, clock_radius * 1.1, -0.01),
    depth=0.1,
)

while True:
    vp.rate(5000)
    hour = tm.localtime(tm.time())[3]
    if hour > 12:
        hour = hour - 12
    minutes = tm.localtime(tm.time())[4]
    seconds = tm.localtime(tm.time())[5]
    second_arrow.axis = vp.vector(
        clock_radius * np.cos(np.deg2rad(theta_seconds)),
        clock_radius * np.sin(np.deg2rad(theta_seconds)),
        0.0,
    )
    minute_arrow.axis = vp.vector(
        arrow_length * np.cos(np.deg2rad(theta)),
        arrow_length * np.sin(np.deg2rad(theta)),
        0.0,
    )
    hour_arrow.axis = vp.vector(
        hour_arrow_length * np.cos(np.deg2rad(theta_hour)),
        hour_arrow_length * np.sin(np.deg2rad(theta_hour)),
        0.0,
    )
    theta_seconds = -(seconds / 60) * 360 + 90
    theta = -(minutes / 60) * 360 + 90 - 6 * (seconds / 60)
    theta_hour = -(hour / 12) * 360 + 90 - 30 * (minutes / 60)
