import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length,index):
    t.color(colorList[index])
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()
colorList = ["red", "blue", "green"]
x = -200

for i in range(len(colorList)):
    t.up()
    t.goto(x,0)
    t.down()
    square(100,i);
    x+=200