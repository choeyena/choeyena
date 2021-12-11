import turtle
import math

t = turtle.Turtle()
t.shape("turtle")
t.color('red', 'yellow')
for x in range(0, 360):
    t.goto(x,200*math.sin(x*3.14/180))