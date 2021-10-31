import turtle
t = turtle. Turtle()
t.shape("turtle")

radius=50
t.up()
t.goto(0, 0)
t.down()
t.circle(radius)

radius = radius + 20
t.up()
t.goto(100, 0)
t.down()
t.circle(radius)

radius = radius + 20
t.up()
t.goto(200, 0)
t.down()
t.circle(radius)
t._screen.exitonclick()