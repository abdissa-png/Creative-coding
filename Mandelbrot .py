import math
import turtle
a=turtle.Turtle()
a.speed(0)
a.pencolor("red")
def draw():
	for i in range(-200,201,1):
		for j in range(-200,201,1):
			if (mandelbrot([0,0],[i/100,j/100],0)):
				a.penup()
				a.goto([i,j])
				a.pendown()
				a.circle(2)
def mandelbrot(arr,offset,count):
	if (math.sqrt((arr[0]**2)+(arr[1]**2))<=2) and count>100:
		return True
	elif math.sqrt((arr[0]**2)+(arr[1]**2))>2:
		return False
	else:
		x=arr[0]**2-arr[1]**2+offset[0]
		y=2*arr[0]*arr[1]+offset[1]
		arr=[x,y]
		count+=1
		return mandelbrot(arr,offset,count)
draw()
turtle.done()
