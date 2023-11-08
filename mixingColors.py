import vpython as vp
import numpy as np

# initializing
my_sphere = vp.sphere(radius=1, color=vp.vector(1, 1, 0))


red = 1
green = 1
blue = 0
red_delta = 0.01
green_delta = -0.01
blue_delta = 0.01
while True:
    vp.rate(50)

    red += red_delta
    green += green_delta
    blue += blue_delta

    if red <= 1:
        red_apply = red
    if red > 1:
        red_apply = 1

    if green <= 1:
        green_apply = green
    if green > 1:
        green_apply = 1

    if blue <= 1:
        blue_apply = blue
    if blue > 1:
        blue_apply = 1

    my_sphere.color = vp.vector(red_apply, green_apply, blue_apply)

    if red >= 1.5 or red <= 0:
        red_delta = -red_delta

    if green >= 1.5 or green <= 0:
        green_delta = -green_delta

    if blue >= 1.5 or blue <= 0:
        blue_delta = -blue_delta

    print(red_apply + green_apply + blue_apply)


""" 
    if red >= 1 or red <= 0:
        red_delta = -red_delta
    if green >= 1 or green <= 0:
        green_delta = -green_delta
    if blue >= 1 or blue <= 0:
        blue_delta = -blue_delta


    if (red + green + blue >= 1.9 and red + green + blue <= 2.1 ):
        my_sphere.color = vp.vector(red, green, blue) """
