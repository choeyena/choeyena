import turtle
t = turtle.Turtle()
t.shape("turtle")

def shape(length):
    s = turtle.textinput("","몇각형을 원하시나요? : ")
    n = int(s)
    
    for i in range(n):
        t.forward(length)
        t.left(360/n)
        
t.up()
t.goto(-200,0)
t.down()
shape(100);

t. up()
t.goto(200,0)
t.down()
shape(100);
