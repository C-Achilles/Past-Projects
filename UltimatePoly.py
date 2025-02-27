import turtle
import random

colours = ["AntiqueWhite", "AntiqueWhite4", "aquamarine", "aquamarine4", "azure4", "beige", "bisque", "BlanchedAlmond", "blue", "BlueViolet", "brown", "burlywood",
           "CadetBlue", "chartreuse", "chocolate", "coral", "CornflowerBlue", "cornsilk", "cyan", "DarkBlue", "DarkGoldenrod", "DarkGrey", "DarkGreen", "DarkKhaki", "DarkMagenta",
           "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray1", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue"]

def ultimatePoly(sideLength, noOfSides, colour, thickness):
    tess.color(colour)
    tess.pensize(thickness)
    for myMoves in range(noOfSides):
        tess.forward(sideLength)
        tess.left(360/noOfSides)

wn = turtle.Screen()
wn.bgcolor("white")

tess = turtle.Turtle()
tess.speed(1000)
tess.hideturtle()

noOfShapes = 120
noOfSides = 5
size = 100
for myMoves in range(noOfShapes):
    colour = colours[random.randint(0,len(colours)-1)]
    tess.color(colour)
    ultimatePoly(size, noOfSides, colour, 3)
    tess.left(360/noOfShapes)

wn.mainloop()
