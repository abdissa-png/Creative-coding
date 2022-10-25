import math
import time
import random
import turtle as t
from turtle import Screen
a=t.Turtle()
cd=int()
def cardiod(multiplier,points,size):
	global a
	global cd
	cd=size
	screen=Screen()
	screen.colormode(255)
	a.speed(0)
	a.pencolor(255,0,0)
	arr=[]
	arr.append([size,0])
	angle=360/points
	for i in range(1,points):
		x=size*math.cos(math.radians(i*angle))
		y=size*math.sin(math.radians(i*angle))
		arr.append([x,y])
	now=1
	a.penup()
	a.goto(arr[0])
	a.pendown()
	a.penup()
	a.goto(arr[0])
	a.goto(arr[1])
	a.pendown()
	for i in range(1,points):
		a.pendown()
		p=["red","orange","yellow","green","blue","indigo","violet"]
		#a.pencolor(random.randint(60,255),random.randint(50,255),random.randint(0,250))
		a.pencolor(p[i%7])
		a.goto(arr[int((multiplier*i)%points)])
		a.penup()
		a.goto(arr[(i+1)%points])
'''a.pencolor("red")
a.penup()
a.goto([0,-385])
a.pendown()
a.circle(385)'''
for i in range(20,31,1):
	j=101
	cardiod((i/10),j,385)
	time.sleep(1.7)
	t.clearscreen()
t.done()	
