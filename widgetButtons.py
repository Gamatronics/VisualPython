from vpython import *
from time import *

mRadius = 0.5
wallThickness = 0.1
roomWidth = 12
roomDepth = 20
roomHeight = 15
floor = box(
    pos=vector(0, -roomHeight / 2, 0),
    size=vector(roomWidth, wallThickness, roomDepth),
    color=color.white,
)
ceiling = box(
    pos=vector(0, roomHeight / 2, 0),
    size=vector(roomWidth, wallThickness, roomDepth),
    color=color.white,
)
backWall = box(
    pos=vector(0, 0, -roomDepth / 2),
    size=vector(roomWidth, roomHeight, wallThickness),
    color=color.white,
)
leftWall = box(
    pos=vector(-roomWidth / 2, 0, 0),
    size=vector(wallThickness, roomHeight, roomDepth),
    color=color.white,
)
rightWall = box(
    pos=vector(roomWidth / 2, 0, 0),
    size=vector(wallThickness, roomHeight, roomDepth),
    color=color.white,
)
marble = sphere(radius=mRadius, color=color.white)
deltaX = 0.1
deltaY = 0.1
deltaZ = 0.1

xPos = 0
yPos = 0
zPos = 0

run = 0
mySpeed = 1


def runRadio(x):
    print(x.checked)
    global run
    if x.checked == True:
        run = 1
    else:
        run = 0


def big_ball(x):
    global mRadius
    if x.checked == True:
        mRadius = mRadius * 2
        marble.radius = mRadius
    if x.checked == False:
        mRadius = mRadius / 2
        marble.radius = mRadius


def ballColorGreen(x):
    marble.color = color.green


def ballColorRed(x):
    marble.color = color.red


button(bind=ballColorRed, text="Red", color=color.black, background=color.red)

button(bind=ballColorGreen, text="Green", color=color.black, background=color.green)


def ballColorBlue(x):
    marble.color = color.blue


button(bind=ballColorBlue, text="Blue", color=color.black, background=color.blue)


def ballOpacity(x):
    op = x.value
    marble.opacity = op


def speed(x):
    global mySpeed
    if x.selected == "1":
        mySpeed = 1
    if x.selected == "2":
        mySpeed = 2
    if x.selected == "3":
        mySpeed = 3
    if x.selected == "4":
        mySpeed = 4
    if x.selected == "5":
        mySpeed = 5


scene.append_to_caption("\n\n")
radio(bind=runRadio, text="Run")
scene.append_to_caption("     ")
checkbox(bind=big_ball, text="Big Ball")
wtext(text="\n\nSelect ball speed\n\n")
menu(bind=speed, choices=["1", "2", "3", "4", "5"])
scene.append_to_caption("\n\n")

wtext(text="Choose your opacity")
scene.append_to_caption("\n\n")
slider(bind=ballOpacity, vertical=False, min=0, max=1, value=1)
scene.append_to_caption("\n\n")


while True:
    rate(25)

    xPos = xPos + deltaX * run * mySpeed
    yPos = yPos + deltaY * run * mySpeed
    zPos = zPos + deltaZ * run * mySpeed

    Xrme = xPos + mRadius
    Xlme = xPos - mRadius
    Ytme = yPos + mRadius
    Ybme = yPos - mRadius
    Zbme = zPos - mRadius
    Zfme = zPos + mRadius

    Rwe = roomWidth / 2 - wallThickness / 2
    Lwe = -roomWidth / 2 + wallThickness / 2
    Cwe = roomHeight / 2 - wallThickness / 2
    FLOORwe = -roomHeight / 2 + wallThickness / 2
    Bwe = -roomDepth / 2 + wallThickness / 2
    Fwe = roomDepth / 2 - wallThickness / 2

    if Xrme >= Rwe or Xlme <= Lwe:
        deltaX = deltaX * (-1)

    if Ytme >= Cwe or Ybme <= FLOORwe:
        deltaY = deltaY * (-1)

    if Zfme >= Fwe or Zbme <= Bwe:
        deltaZ = deltaZ * (-1)

    marble.pos = vector(xPos, yPos, zPos)
