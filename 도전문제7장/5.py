import turtle
import random

def tree(length):
    angle = (random.randint(-20,20))
    if length > 5:
        t.forward(length)
        t.right(20 + angle)
        tree(length-15 *(random.random()+0.4))
        t.left(40 + (angle * 2))
        tree(length-15 *(random.random()+0.4))
        t.right(20 + angle)
        t.backward(length)
        
t = turtle.Turtle()
t.left(90)

t.color("green")
t.spees(1)
tree(90)