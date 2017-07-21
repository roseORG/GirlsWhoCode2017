from turtle import *
import math

Turtle
t = Turtle()

# Set Up your screen and starting position.p
t.penup()
setup(500,300)
x_pos = 0
y_pos = 0

t.setposition(x_pos, y_pos)
t.pendown()
for counter in range(4):
    t.forward(25)
    t.right(90)
t.penup()
### Write your code below:
exitonclick()
