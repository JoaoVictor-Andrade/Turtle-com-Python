
from turtle import *

from random import *


BODY_COLOR = 'red'
BODY_SHADOW = ''
GLASS_COLOR = '#9acedc'
GLASS_SHADOW = ''

t = Turtle()
t.penup()
t.setpos(500, -100)
t.pendown()



def body():

    t.pensize(10)
    # t.speed(15)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    # right side
    t.right(45)
    t.forward(25)
    t.right(90)
    t.circle(20, -90)
    t.right(90)
    t.forward(100)

    # head curve
    t.right(90)
    t.circle(60, -90)

    # left side
    t.backward(10)
    t.left(7.5)
    t.circle(250, -10)
    t.backward(10)

    # t.backward(200)
    t.circle(20, -90)
    # t.right(90)
    t.left(3.5)
    t.backward(25)

    # hip
    t.up()
    t.left(45)
    t.forward(5)
    t.right(45)
    t.down()
    # t.right(180)
    # t.circle(25, -180)
    t.right(120)
    t.circle(25, -30)

    t.end_fill()


def glass():
    t.up()
    # t.right(180)
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.down()
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    # t.right(180)
    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()


def backpack():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(35)

    t.end_fill()

body()
glass()
backpack()



hideturtle()
exitonclick()