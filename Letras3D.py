import vpython as vp
import numpy as np
import random

global spacing
spacing = 0.2


def h(h_radius=0.1, h_length=1, index=0, ruler_on=0, color=[1, 0, 1]):
    # h_radius = 0.1
    # h_length = 1
    h_position = h_length / 2
    horizontal_separation = 3 * h_radius
    width = (horizontal_separation * 2) + (2 * h_radius) + spacing
    ruler_length = (horizontal_separation * 2) + (2 * h_radius)

    left_h = vp.cylinder(
        radius=h_radius,
        length=h_length,
        color=vp.vector(color[0], color[1], color[2]),
        axis=vp.vector(0, 1, 0),
        pos=vp.vector(width * (index) - horizontal_separation, -h_position, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    right_h = vp.cylinder(
        radius=h_radius,
        length=h_length,
        color=vp.vector(color[0], color[1], color[2]),
        axis=vp.vector(0, 1, 0),
        pos=vp.vector(width * (index) + horizontal_separation, -h_position, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    middle_h = vp.cylinder(
        radius=h_radius,
        length=horizontal_separation * 2,
        color=vp.vector(color[0], color[1], color[2]),
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(width * (index) - horizontal_separation, 0, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    ruler = vp.cylinder(
        radius=0.010,
        length=ruler_length,
        color=vp.color.orange,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(-(horizontal_separation + h_radius), h_length / 2, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=ruler_on,
    )


def o(size=0.4, index=0, is_space=False):
    width = size * 2 + spacing
    if is_space:
        opacity = 0
    else:
        opacity = 1

    sphere = vp.sphere(
        radius=size,
        color=vp.color.white,
        pos=vp.vector(width * index, 0, 0),
        opacity=opacity,
    )


def l(h_radius=0.1, h_length=1, index=0, ruler_on=0):
    # width =
    h_position = h_length / 2
    horizontal_separation = 3 * h_radius
    width = (horizontal_separation * 2) + h_radius * 2 + spacing
    ruler_length = (horizontal_separation * 2) + h_radius * 2

    left_h = vp.cylinder(
        radius=h_radius,
        length=h_length,
        color=vp.color.red,
        axis=vp.vector(0, 1, 0),
        pos=vp.vector(width * (index) - horizontal_separation, -h_position, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    middle_h = vp.cylinder(
        radius=h_radius,
        length=horizontal_separation * 2,
        color=vp.color.red,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(
            width * (index) - horizontal_separation, -h_position + h_radius, 0
        ),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    ruler = vp.cylinder(
        radius=0.010,
        length=ruler_length,
        color=vp.color.orange,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(-(horizontal_separation + h_radius), -h_length / 2, 0),
        # pos = vp.vector(-(horizontal_separation + h_radius),-0,0),
        opacity=ruler_on,
    )


def c(h_radius=0.1, h_length=1, index=0, ruler_on=0):
    # width =
    h_position = h_length / 2
    horizontal_separation = 3 * h_radius
    width = (horizontal_separation * 2) + h_radius * 2 + spacing
    ruler_length = (horizontal_separation * 2) + h_radius * 2

    left_h = vp.cylinder(
        radius=h_radius,
        length=h_length,
        color=vp.color.red,
        axis=vp.vector(0, 1, 0),
        pos=vp.vector(width * (index) - horizontal_separation, -h_position, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    bottom_h = vp.cylinder(
        radius=h_radius,
        length=horizontal_separation * 2,
        color=vp.color.red,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(
            width * (index) - horizontal_separation, -h_position + h_radius, 0
        ),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    top_h = vp.cylinder(
        radius=h_radius,
        length=horizontal_separation * 2,
        color=vp.color.red,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(
            width * (index) - horizontal_separation, +h_position - h_radius, 0
        ),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    ruler = vp.cylinder(
        radius=0.010,
        length=ruler_length,
        color=vp.color.orange,
        axis=vp.vector(1, 0, 0),
        # pos = vp.vector(-(horizontal_separation + h_radius),-h_length/2,0),
        pos=vp.vector(-(horizontal_separation + h_radius), -0, 0),
        opacity=ruler_on,
    )


def u(h_radius=0.1, h_length=1, index=0, ruler_on=0):
    # width =
    h_position = h_length / 2
    horizontal_separation = 3 * h_radius
    width = (horizontal_separation * 2) + h_radius * 2 + spacing
    ruler_length = (horizontal_separation * 2) + h_radius * 2

    left_h = vp.cylinder(
        radius=h_radius,
        length=h_length,
        color=vp.color.red,
        axis=vp.vector(0, 1, 0),
        pos=vp.vector(width * (index) - horizontal_separation, -h_position, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    right_h = vp.cylinder(
        radius=h_radius,
        length=h_length,
        color=vp.color.red,
        axis=vp.vector(0, 1, 0),
        pos=vp.vector(width * (index) + horizontal_separation, -h_position, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    bottom_h = vp.cylinder(
        radius=h_radius,
        length=horizontal_separation * 2,
        color=vp.color.red,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(
            width * (index) - horizontal_separation, -h_position + h_radius, 0
        ),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    ruler = vp.cylinder(
        radius=0.010,
        length=ruler_length,
        color=vp.color.orange,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(-(horizontal_separation + h_radius), -h_length / 2, 0),
        # pos = vp.vector(-(horizontal_separation + h_radius),-0,0),
        opacity=ruler_on,
    )


def a(h_radius=0.1, h_length=1, index=0, ruler_on=0):
    # width =
    h_position = h_length / 2
    horizontal_separation = 3 * h_radius
    width = (horizontal_separation * 2) + h_radius * 2 + spacing
    ruler_length = (horizontal_separation * 2) + h_radius * 2

    left_h = vp.cylinder(
        radius=h_radius,
        length=h_length,
        color=vp.color.red,
        axis=vp.vector(0.30, 1, 0),
        pos=vp.vector(width * (index) - horizontal_separation, -h_position, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    right_h = vp.cylinder(
        radius=h_radius,
        length=h_length,
        color=vp.color.red,
        axis=vp.vector(-0.30, 1, 0),
        pos=vp.vector(width * (index) + horizontal_separation, -h_position, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    middle_h = vp.cylinder(
        radius=h_radius,
        length=horizontal_separation * 2,
        color=vp.color.red,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(width * (index) - horizontal_separation, -0.25 * h_length, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    ruler = vp.cylinder(
        radius=0.010,
        length=ruler_length,
        color=vp.color.orange,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(-(horizontal_separation + h_radius), -h_length / 2, 0),
        # pos = vp.vector(-(horizontal_separation + h_radius),-0,0),
        opacity=ruler_on,
    )


def i(h_radius=0.1, h_length=1, index=0, ruler_on=0):
    # width =
    h_position = h_length / 2
    horizontal_separation = 3 * h_radius
    width = (horizontal_separation * 2) + h_radius * 2 + spacing
    ruler_length = (horizontal_separation * 2) + h_radius * 2

    center_h = vp.cylinder(
        radius=h_radius,
        length=h_length,
        color=vp.color.red,
        axis=vp.vector(0, 1, 0),
        pos=vp.vector(width * (index), -h_position, 0),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    bottom_h = vp.cylinder(
        radius=h_radius,
        length=horizontal_separation * 2,
        color=vp.color.red,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(
            width * (index) - horizontal_separation, -h_position + h_radius, 0
        ),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    top_h = vp.cylinder(
        radius=h_radius,
        length=horizontal_separation * 2,
        color=vp.color.red,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(
            width * (index) - horizontal_separation, +h_position - h_radius, 0
        ),
        # pos = vp.vector(horizontal_separation*(index),-h_position,0),
        opacity=1,
    )

    ruler = vp.cylinder(
        radius=0.010,
        length=ruler_length,
        color=vp.color.orange,
        axis=vp.vector(1, 0, 0),
        pos=vp.vector(-(horizontal_separation + h_radius), -h_length / 2, 0),
        # pos = vp.vector(-(horizontal_separation + h_radius),-0,0),
        opacity=ruler_on,
    )


h(index=0, ruler_on=0)
o(index=1)
l(index=2, ruler_on=0)
a(index=3, ruler_on=0)

o(index=4, is_space=True)

c(index=5)
u(index=6)
c(index=7)
h(index=8)
i(index=9, ruler_on=0)

o(index=10, is_space=True)
c(index=11)
u(index=12)
c(index=13)
h(index=14)
i(index=15, ruler_on=0)

# vp.scene.camera.pos = vp.vector(7.5,0,-7)
while True:
    pass
