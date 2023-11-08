import vpython as vp
import numpy as np


arrow_length = 2
pointer_length = 2
arrow_thick = 0.02
theta = np.pi / 4
theta_degrees = 89
Xarrow = vp.arrow(
    color=vp.color.red,
    length=arrow_length,
    shaftwidth=arrow_thick,
    axis=vp.vector(1, 0, 0),
)
Yarrow = vp.arrow(
    color=vp.color.green,
    length=arrow_length,
    shaftwidth=arrow_thick,
    axis=vp.vector(0, 1, 0),
)
Zarrow = vp.arrow(
    color=vp.color.blue,
    length=arrow_length,
    shaftwidth=arrow_thick,
    axis=vp.vector(0, 0, 1),
)

pointer_arrow = vp.arrow(
    color=vp.color.orange,
    length=arrow_length,
    shaftwidth=arrow_thick,
    axis=vp.vector(
        arrow_length * np.cos(np.deg2rad(theta_degrees)),
        arrow_length * np.sin(np.deg2rad(theta_degrees)),
        0,
    ),
)
ball = vp.sphere(
    radius=0.05, color=vp.color.white, make_trail=True, trail_color=vp.color.orange
)

theta = 0
theta_delta = 0.5
while True:
    for angle in np.linspace(0, 359, 1000):
        vp.rate(300)
        pointer_arrow.axis = vp.vector(
            pointer_length * np.cos(np.deg2rad(angle)),
            pointer_length * np.sin(np.deg2rad(angle)),
            0,
        )
        ball.pos = vp.vector(
            pointer_length * np.cos(np.deg2rad(angle)),
            pointer_length * np.sin(np.deg2rad(angle)),
            0,
        )
    for angle in np.linspace(0, 359 + 90, 1000):
        vp.rate(300)
        pointer_arrow.axis = vp.vector(
            pointer_length * np.cos(np.deg2rad(angle)),
            0,
            pointer_length * np.sin(np.deg2rad(angle)),
        )
        ball.pos = vp.vector(
            pointer_length * np.cos(np.deg2rad(angle)),
            0,
            pointer_length * np.sin(np.deg2rad(angle)),
        )
    for angle in np.linspace(0, 359, 1000):
        vp.rate(300)
        pointer_arrow.axis = vp.vector(
            0,
            pointer_length * np.sin(np.deg2rad(angle)),
            pointer_length * np.cos(np.deg2rad(angle)),
        )
        ball.pos = vp.vector(
            0,
            pointer_length * np.sin(np.deg2rad(angle)),
            pointer_length * np.cos(np.deg2rad(angle)),
        )
    for angle in np.linspace(90, 359, 1000):
        vp.rate(300)
        pointer_arrow.axis = vp.vector(
            pointer_length * np.cos(np.deg2rad(angle)),
            0,
            pointer_length * np.sin(np.deg2rad(angle)),
        )
        ball.pos = vp.vector(
            pointer_length * np.cos(np.deg2rad(angle)),
            0,
            pointer_length * np.sin(np.deg2rad(angle)),
        )
    pass
