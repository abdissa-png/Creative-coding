import turtle
import math
a=turtle.Turtle()
a.speed(0)
def draw(size,init,dest,branch):
	if size>10:
		a.penup()
		a.goto(init)
		a.pendown()
		a.goto(dest)
		c=5/7
		angle=[0]*branch
		if branch%2==0:
			for i in range(branch):
				if i<(branch//2):
					angle[i]=((branch//2)-i)*90/branch
				else:
					angle[i]=90+((i+1-(branch//2))*90/branch)
		else:
			for i in range(branch):
				if i<(branch//2):
					angle[i]=((branch//2)-i)*90/branch
				elif (i==(branch//2)):
					angle[i]=0
				else:
					angle[i]=90+((i-(branch//2))*90/branch)
		for i in range(branch):
			if angle[i]<90:
				draw(c*size,dest,[(dest[0]+c*size*math.sin(angle[i])),dest[1]+c*size*math.cos(math.radians(angle[i]))],branch)
			else:
				draw(c*size,dest,[(dest[0]-c*size*math.sin(angle[i]-90)),dest[1]+c*size*math.cos(math.radians(angle[i]-90))],branch)
draw(200,[0,-550],[0,-350],2)
turtle.done()
