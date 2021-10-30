import turtle

t = turtle. Turtle()

t.width(3)

t.shape("turtle")

t.shapesize(3, 3)




while answer:
    command = input("명령을 입력하시오: ")
    if command == "l" or command == "left":
        t.left(90)
        t.forward(100)
    if command == "r" or command == "right":
        t.right(90)
        t.forward(100)