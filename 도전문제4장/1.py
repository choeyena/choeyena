import turtle
t = turtle. Turtle()
t.shape("turtle")

s = turtle. textinput("","이름을 읍력하시오: ")

for i in range(4):
    t.write("안녕하세요?" + s + "씨, 터틀 인사드립니다.")
    t.left(90)
    t.forward(100)