import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def hexagon():
    for i in range(6):
        turtle.forward(100)
        turtle.left(360/6)
        
for i in range (6):
        hexagon()
        turtle.forward(100)
        turtle.right(60)