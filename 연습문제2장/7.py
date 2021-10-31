import turtle
t = turtle. Turtle()
t.shape("turtle")
side = 50
angle = 90

t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side)

t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side)

t.right(angle); t.forward(100); t.right(180)

t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side)

t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side)
t.write("닫으려면 화면 클릭"); t._screen.exitonclick()