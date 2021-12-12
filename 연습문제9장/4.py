import turtle
import random
t = turtle.Turtle()
t.shape("turtle")

def draw_square(x, y, c):
    t.up()
    t.goto(x, y)
    t.down()
    t.color("black",c)
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.end_fill()
    
    for c in ["yellow", "red", "purple", "blue"]:
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        draw_square(x, y, c)