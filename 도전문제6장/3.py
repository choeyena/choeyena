import turtle
import random
t = turtle.Turtle()
t.shape("turtle")

for i in range(30):
    length = random.randint(1,100)
    t.forward(length)
    angle = random.randint(1,4)
    t.right(90 * angle)