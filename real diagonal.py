len=180
s=7
n=s
k=s
import math
import turtle
a=turtle.Turtle()
b=180-(90*(1-(2/n)))
c=len/(2*math.sin(math.radians(180/n)))
d=360/n
e=2*len*(math.sin(math.radians(90*(1-2/n))))
f=180*(1-2/n)
a.right(90)
a.penup()
a.forward(300)
a.pendown()
a.right(90)
for i in range(s):
	if n%2==0:
		a.forward(len)
		a.left(180)
		for i in range(k-3):
			a.left(f/(n-2))
			a.forward(c)
			a.left(180)
			a.forward(c)
			a.left(180)
		a.left(f/(n-2))
	else:
		a.forward(len)
		a.left(180)
		for i in range(k-3):
			a.left(f/(n-2))
			a.forward(c)
			a.left(180)
			a.forward(c)
			a.left(180)
		a.left(f/(n-2))
turtle.done()
