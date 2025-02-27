import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.hideturtle()
t.speed(1000)
r = 5

for i in range(500):
    t.circle(r + i, 45)
