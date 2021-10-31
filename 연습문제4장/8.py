import turtle
t = turtle. Turtle()
t.shape("turtle")

lista = [ ]
lista.append(int(input("x1: ")))
lista.append(int(input("y1: ")))
lista.append(int(input("x2: ")))
lista.append(int(input("y2: ")))
lista.append(int(input("x3: ")))
lista.append(int(input("y3: ")))

t.goto(lista[0], lista[1])
t.goto(lista[2], lista[3])
t.goto(lista[4], lista[5])
t._screen.exitonclick()