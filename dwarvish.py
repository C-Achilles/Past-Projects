import turtle

sentence = str(input("Enter your sentence here: "))
wn = turtle.Screen()

t = turtle.Turtle()
t.hideturtle()
turtle.tracer(0)
size = 70
t.penup()
t.goto(-250, 250)
t.pendown()


def drawA():
    t.setheading(90)
    t.forward(size)
    t.setheading(310)
    t.forward(size/2.5)
    t.backward(size/2.5)
    t.setheading(270)
    t.forward(size/3)
    t.setheading(310)
    t.forward(size/2.5)
    t.backward(size/2.5)
    t.setheading(270)
    t.backward(size/3)
    t.forward(size)

def drawB():
    t.setheading(90)
    t.forward(size)
    t.setheading(330)
    t.forward(size/2)
    t.setheading(210)
    t.forward(size/2)
    t.setheading(330)
    t.forward(size/2)
    t.setheading(210)
    t.forward(size/2)
    t.penup()
    t.setheading(0)
    t.forward(size/3)

def drawC():
    t.setheading(90)
    t.forward(size)
    t.backward(size)
    t.forward(size/2.5)
    t.setheading(300)
    t.forward(size/2.1)
    t.penup()
    t.backward(size/2.1)
    t.setheading(270)
    t.forward(size/2.5)

def drawD():
    t.setheading(90)
    t.forward(size)
    t.setheading(300)
    t.forward(size*1.15)
    t.setheading(90)
    t.forward(size)
    t.setheading(240)
    t.forward(size*1.15)
    t.penup()
    t.setheading(0)
    t.forward(size/3)

def drawE():
    t.setheading(90)
    t.forward(size)
    t.setheading(310)
    t.forward(size/2)
    t.setheading(50)
    t.forward(size/2)
    t.setheading(270)
    t.forward(size)
    t.penup()
    t.setheading(180)
    t.forward(size/3)
    
def drawF():
    t.setheading(90)
    t.forward(size)
    t.backward(size/4)
    t.setheading(40)
    t.forward(size/2.7)
    t.backward(size/2.7)
    t.setheading(90)
    t.forward(size/4)
    t.backward(size/2)
    t.setheading(40)
    t.forward(size/1.3)
    t.penup()
    t.backward(size/1.3)
    t.setheading(270)
    t.forward(size/2)
    t.penup()
    t.setheading(0)
    t.forward(size/3)

def drawG():
    t.penup()
    t.setheading(90)
    t.forward(size)
    t.pendown()
    t.setheading(300)
    t.forward(size*1.15)
    t.setheading(90)
    t.penup()
    t.forward(size)
    t.pendown()
    t.setheading(240)
    t.forward(size*1.15)
    t.penup()
    t.setheading(0)
    t.forward(size/3)

def drawH():
    t.setheading(90)
    t.forward(size)
    t.backward(size/5)
    t.setheading(330)
    t.forward(size/2)
    t.setheading(90)
    t.forward(size/2.2)
    t.backward(size)
    t.forward(size/2.8)
    t.setheading(150)
    t.forward(size/2)
    t.setheading(270)
    t.forward(size/1.6)
    t.penup()
    t.setheading(0)
    t.forward(size/3)

def drawI():
    t.penup()
    t.setheading(0)
    t.forward(size/3)
    t.pendown()
    t.setheading(90)
    t.forward(size)
    t.backward(size)

def drawJ():
    t.setheading(90)
    t.forward(size)
    t.backward(size/4)
    t.setheading(330)
    t.forward(size/3)
    t.setheading(90)
    t.forward(size/2.5)
    t.penup()
    t.backward(size/2.5)
    t.setheading(150)
    t.forward(size/3)
    t.setheading(270)
    t.forward((size/4)*2)
    t.setheading(150)
    t.pendown()
    t.forward(size/3)
    t.setheading(270)
    t.forward(size/2.5)
    t.penup()
    t.backward(size/2.5)
    t.setheading(330)
    t.forward(size/3)
    t.setheading(270)
    t.forward(size/4)

def drawK():
    t.setheading(90)
    t.forward(size)
    t.backward(size/2)
    t.setheading(330)
    t.forward(size/2)
    t.setheading(270)
    t.forward(size/4)
    t.penup()
    t.backward(size/4)
    t.setheading(150)
    t.forward(size/2)
    t.setheading(270)
    t.forward(size/2)
    t.setheading(0)
    t.forward(size/4)

def drawL():
    t.setheading(90)
    t.forward(size)
    t.setheading(300)
    t.forward(size/2.5)
    t.penup()
    t.backward(size/2.5)
    t.setheading(270)
    t.forward(size)

def drawM():
    t.setheading(90)
    t.forward(size)
    t.setheading(330)
    t.forward(size)
    t.setheading(90)
    t.forward(size/2)
    t.setheading(210)
    t.forward(size)
    t.setheading(30)
    t.forward(size)
    t.setheading(270)
    t.forward(size)

def drawN():
    t.penup()
    t.setheading(0)
    t.forward(size/3)
    t.pendown()
    t.setheading(90)
    t.forward(size)
    t.backward(size/2)
    t.setheading(150)
    t.forward(size/3)
    t.backward(size/3)
    t.backward(size/3)
    t.forward(size/3)
    t.setheading(270)
    t.forward(size/2.5)
    t.penup()
    t.backward(size/2.5)
    t.setheading(270)
    t.forward(size/2)

def drawO():
    t.setheading(90)
    t.forward(size)
    t.setheading(330)
    t.forward(size/3)
    t.setheading(30)
    t.forward(size/3)
    t.penup()
    t.setheading(270)
    t.forward(size/4)
    t.pendown()
    t.setheading(210)
    t.forward(size/3)
    t.setheading(150)
    t.forward(size/3)
    t.setheading(270)
    t.penup()
    t.forward((size/4)*3)
    t.setheading(0)
    t.forward(size/2)
    

def drawP():
    t.setheading(90)
    t.forward(size)
    t.backward(size/5)
    t.setheading(330)
    t.forward(size/2.5)
    t.setheading(90)
    t.forward(size/2.5)
    t.penup()
    t.backward(size)
    t.pendown()
    t.forward(size/2.5)
    t.setheading(210)
    t.forward(size/2.5)
    t.setheading(270)
    t.forward(size/4)

def drawQ():
    t.setheading(90)
    t.forward(size)
    t.penup()
    t.backward(size/1.9)
    t.pendown()
    t.setheading(330)
    t.forward(size/2)
    t.setheading(270)
    t.forward(size/4)
    t.setheading(150)
    t.forward(size/2)
    t.setheading(270)
    t.forward(size/4)
    t.penup()
    t.setheading(0)
    t.forward(size/4)

def drawR():
    t.setheading(90)
    t.forward(size)
    t.setheading(330)
    t.forward(size/2)
    t.setheading(210)
    t.forward(size/2)
    t.setheading(310)
    t.forward(size/1.5)
    t.backward(size/1.5)
    t.setheading(270)
    t.forward(size/2)
    t.penup()
    t.setheading(0)
    t.forward(size/3)

def drawS():
    t.penup()
    t.setheading(90)
    t.forward(size)
    t.setheading(270)
    t.pendown()
    t.forward(size/1.7)
    t.setheading(40)
    t.forward(size/4)
    t.setheading(270)
    t.forward(size/1.7)

def drawT():
    t.setheading(90)
    t.forward(size)
    t.setheading(240)
    t.forward(size/3)
    t.backward(size/3)
    t.setheading(300)
    t.forward(size/3)
    t.penup()
    t.backward(size/3)
    t.setheading(270)
    t.forward(size)

def drawU():
    t.setheading(90)
    t.penup()
    t.forward(size)
    t.pendown()
    t.backward(size/2)
    t.setheading(310)
    t.forward(size/1.5)
    t.setheading(90)
    t.forward(size)
    t.penup()
    t.backward(size/1.5)
    t.setheading(210)
    t.pendown()
    t.forward(size/4.4)
    t.penup()
    t.backward(size/4.4)
    t.setheading(270)
    t.forward(size/3)
    t.setheading(130)
    t.forward(size/1.5)
    t.setheading(270)
    t.forward(size/2)
    t.setheading(0)
    t.forward(size/3)
    
def drawV():
    t.setheading(90)
    t.forward(size)
    t.setheading(310)
    t.forward(size/1.5)
    t.setheading(270)
    t.forward(size/2)

def drawW():
    t.setheading(90)
    t.forward(size)
    t.setheading(330)
    t.forward(size/2)
    t.setheading(210)
    t.forward(size/2)
    t.setheading(270)
    t.forward(size/2)

def drawX():
    t.setheading(90)
    t.forward(size)
    t.backward(size/2)
    t.setheading(120)
    t.forward(size/1.7)
    t.backward(size/1.7)
    t.setheading(60)
    t.forward(size/1.7)
    t.penup()
    t.setheading(0)
    t.forward(size/3)

def drawY():
    t.setheading(90)
    t.forward(size)
    t.setheading(340)
    t.forward(size/1.5)
    t.setheading(270)
    t.forward(size/1.3)
    t.backward(size/1.8)
    t.setheading(160)
    t.forward(size/1.5)
    t.penup()
    t.backward(size/3)
    t.pendown()
    t.setheading(270)
    t.forward(size/1.5)

def drawZ():
    t.setheading(90)
    t.forward(size)
    t.backward(size/2)
    t.setheading(240)
    t.forward(size/1.7)
    t.backward(size/1.7)
    t.setheading(300)
    t.forward(size/1.7)




noOfWords = False

listOfSentence = list(sentence)
position = 250
for letter in range(len(listOfSentence)):
    t.pendown()
    if listOfSentence[letter].upper() == "A":
        drawA()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "B":
        drawB()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "C":
        drawC()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "D":
        drawD()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "E":
        drawE()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "F":
        drawF()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "G":
        drawG()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "H":
        drawH()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "I":
        drawI()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "J":
        drawJ()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "K":
        drawK()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "L":
        drawL()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "M":
        drawM()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "N":
        drawN()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "O":
        drawO()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "P":
        drawP()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "Q":
        drawQ()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "R":
        drawR()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        

    elif listOfSentence[letter].upper() == "S":
        drawS()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "T":
        drawT()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "U":
        drawU()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "V":
        drawV()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "W":
        drawW()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "X":
        drawX()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == "Y":
        drawY()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()

    elif listOfSentence[letter].upper() == "Z":
        drawZ()
        t.penup()
        t.setheading(0)
        t.forward(size/2)
        t.pendown()
        
    elif listOfSentence[letter].upper() == " ":
        if noOfWords:
            t.penup()
            position = position - (size*1.5)
            t.goto(-250, position)
            t.pendown()
            noOfWords = False
        else:
            t.penup()
            t.setheading(0)
            t.forward(size)
            t.pendown()
            noOfWords = True


