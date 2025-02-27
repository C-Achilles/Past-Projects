import turtle
wn = turtle.Screen()
wn.bgcolor("blue")

rodney = turtle.Turtle()
rodney.color("turquoise")
rodney.speed(10)

numberOfSides = int(input("enter a number"))

for sides in range (numberOfSides):
    rodney.forward(100)
    rodney.left(360/numberOfSides)
