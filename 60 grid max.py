import turtle
import math
b=turtle.Turtle()
c=0
len=15
b.penup()
b.right(90)
b.forward(350)
b.right(90)
b.forward(680)
b.left(180)
b.pendown()
b.left(90)
while c<24:
    b.forward(len)
    b.right(30)
    b.forward(len)
    b.left(180)
    b.forward(len)
    b.right(120)
    b.forward(len)
    b.right(30)
    c=c+1
b.right(150)
b.forward(len)
b.left(120)
b.forward(len)
b.right(150)
for i in range(100):
    c=0
    while c<24:
        b.forward(len)
        b.right(30)
        b.forward(len)
        b.left(180)
        b.forward(len)
        b.right(120)
        b.forward(len)
        b.right(30)
        c=c+1
    b.left(180)
    while c<48:
        b.forward(len)
        b.right(30)
        b.forward(len)
        b.left(180)
        b.forward(len)
        b.right(120)
        b.forward(len)
        b.right(30)
        c=c+1
    b.right(150)
    b.forward(len)
    b.left(120)
    b.forward(len)
    b.right(150)
turtle.done()
