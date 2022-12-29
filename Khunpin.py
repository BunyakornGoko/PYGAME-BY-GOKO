import turtle
import math
import numpy as np
from  random import randint

s = turtle.getscreen()
t = turtle.Turtle()

t.pen(pencolor="Blue", fillcolor="cyan", pensize=10, speed=20)
t.begin_fill()
t.circle(90)
t.end_fill()

t.penup()
t.goto(100, 250)
t.pendown()
t.forward(100)
t.left(90)

turtle.exitonclick()



