import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

def draw_star(aturtle, color, side_length, x, y):
    aturtle.color(color)
    aturtle.begin_fill()
    aturtle.penup()
    aturtle.goto(x, y)
    aturtle.pendown()
    for i in range(5):
        aturtle.forward(side_length)
        aturtle.right(144)
        aturtle.forward(side_length)
    aturtle.end_fill()
    
    for i in range(20):
        color = random.choice(['white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ])
        side_length = random.randint(10, 100)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        draw_star(t, color, side_length, x,y)