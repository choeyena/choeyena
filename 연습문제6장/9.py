import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for j in range (1,10):
    t.up()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    r = random.randint(10, 200)
    t.goto(x, y)
    t.down()
    t.circle(r)