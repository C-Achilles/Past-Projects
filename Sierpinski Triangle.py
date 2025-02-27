import turtle

def draw_sierpinski(length,depth):
    if depth==0:
        #draw a triangle
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        t.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)

def count_sierpinski(depth):
    global count
    if depth == 0:
        count=1
    else:
        count_sierpinski(depth-1)
        count=count*3
        count+=2
        
        

wn = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(1000)
#turtle.tracer(0)
t.penup()
t.goto(-450, -380)
t.pendown()
count = 1
depth = 2
draw_sierpinski(900,depth) #the right parameter control how deep into recursion you go
count_sierpinski(depth)
print(count)
