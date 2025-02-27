import turtle
def drawSquare():
#This is a function called drawSquare
  for myMoves in range (4):
    tess.forward(100)
    tess.left(360/4)
    
wn = turtle.Screen()
wn.bgcolor("white")

tess = turtle.Turtle()
tess.color("hotpink")
tess.speed(10)

for myMoves in range(36):
  drawSquare()
  tess.left(10)
  
wn.mainloop()

import turtle
def drawSquare():
#This is a function called drawSquare
  for myMoves in range (3):
    tess.forward(100)
    tess.left(360/3)
    
wn = turtle.Screen()
wn.bgcolor("white")

tess = turtle.Turtle()
tess.color("hotpink")
tess.speed(10)

for myMoves in range(36):
  drawSquare()
  tess.left(10)
  
wn.mainloop()
