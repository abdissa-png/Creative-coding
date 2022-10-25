side=10
len=100
s=360/side
import turtle
a=turtle.Turtle()
a.penup()
a.right(90)
a.forward(320)
a.left(90)
a.pendown()
if side%2==0:
    for i in range(int(side/2)):
        a.forward(len)
        a.left(s)
        a.forward(2*len)
        a.left(s)
else:
    for i in range(side):
        a.forward(len)
        a.left(s)
        a.forward(2*len)
        a.left(s)
turtle.done()
