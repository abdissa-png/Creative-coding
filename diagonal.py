len=100
s=7
n=s
import math
import turtle
a=turtle.Turtle()
b=180-(90*(1-(2/n)))
c=len/(2*math.sin(math.radians(180/n)))
d=360/n
e=2*len*(math.sin(math.radians(90*(1-2/n))))
f=180*(1+1/n)
for i in range(s):
	if n%2==0:
		a.forward(len)
		a.right(b)
		a.forward(c)
		a.right(180-d)
		a.forward(c)
		a.right(b)
		a.forward(len)
		a.right(d)
	else:
		a.forward(e)
		a.right(f)
		a.forward(len)
		a.right(f)
		a.forward(e)
		a.right(f)
		a.forward(len)
		a.right(f)
turtle.done()