import turtle
t = turtle.Turtle()

def n_polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360/n)
        
def get_color(index):
    list = ["red", "orange", "yellow", "green", "blue", "navy", "purple", "gray", "skyblue", "pink"]
    t.color(list[index])
    t.begin_fill()
    n_polygon(6,100)
    t.end_fill()
    
for i in range(10):
    t.left(20)
    get_color(i)