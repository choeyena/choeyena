import turtle
t = turtle. Turtle()
t.shape("turtle")

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 

t.up()
t.goto(x1, y1)
t.down()
t.goto(x2, y2)

t.write("점의 길이= " +str(dist))
t._screen.exitonclick()