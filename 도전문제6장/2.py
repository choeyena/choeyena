import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","몇각형을 원하시나요? : ")
n = int(s)
s = turtle.textinput("","한변의 크기를 입력해주세요 :")
len = int(s)
for i in range(n):
    t.forward(len)
    t.left(360/n)