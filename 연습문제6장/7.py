import turtle

t = turtle.Turtle()
t.shape("turtle")
t.left(90)

for i in range(1,7):
    t.forward(100)
    t.forward(-30)
    t.left(60)
    t.forward(30)
    t.forward(-30)
    
    t.right(120)
    t.forward(30)
    t.forward(-30)
    
    t.left(60)
    t.forward(-70)
    t.left(60)