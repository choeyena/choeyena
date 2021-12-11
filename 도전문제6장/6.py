import turtle
import random

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()

turtle.bgcolor("black")

t.speed(0)

t.width(3)

length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    angle = random.randint(1,100)
    t.right(angle)
    length += 5