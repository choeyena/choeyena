import turtle
t = turtle. Turtle()
t.shape("turtle")

lista = [ ]
color = input("색상 #1을 입력하시오: ")
lista. append(color)
color = input("색상 #2을 입력하시오: ")
lista. append(color)
color = input("색상 #3을 입력하시오: ")
lista. append(color)

t.fillcolor(lista[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100, 0)
t.down()
t.fillcolor(lista[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(200, 0)
t.down()
t.fillcolor(lista[2])
t.begin_fill()
t.circle(50)
t.end_fill()
t._screen.exitonclick()