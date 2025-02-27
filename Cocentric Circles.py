import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.hideturtle()
t.speed(1000)
r = 5

for i in range(50):
    t.circle(r * i)
    t.up()
    t.sety((r*i)*(-1))
    t.down()
