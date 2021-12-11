import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def draw_line():
    t.forward(100)
    t.backward(100)
    
for x in range(12):
    t.right(30)
    draw_line()