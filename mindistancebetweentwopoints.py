#brute_force
import math
import copy
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def distance(p1,p2):
    return math.sqrt(((p1.x-p2.x)**2)+((p1.y-p2.y)**2))
def brute_force(P):
    minVal=float(distance(P[0],P[1]))
    n=len(P)
    for i in range(n):
        for j in range((i+1),n):
            if minVal>distance(P[i],P[j]):
                minVal=distance(P[i],P[j])
    return minVal
#n-(logn)^2 time
def compare(P):
    P.sort(key=lambda Point : Point.x)
    upperBoundDis=mergesort(P)
    StripY=[]
    mid=P[len(P)//2]
    for i in range(len(P)):
        if abs(P[i].y-mid.y)<upperBoundDis:
            StripY.append(P[i])
    StripY.sort(key=lambda Point : Point.y)
    minVal=upperBoundDis
    for i in range(len(StripY)-1):
        if distance(StripY[i],StripY[i+1])<upperBoundDis:
            minVal=distance(StripY[i],StripY[i+1])
    return minVal
def mergesort(P):
    if len(P)<=3:
        return brute_force(P)
    else:
        left=P[:len(P)//2]
        right=P[len(P)//2:]
        a=mergesort(left)
        b=mergesort(right)
        return min(a,b)
print(brute_force([Point(2,3),Point(12,30),Point(40,50),Point(5,1),Point(12,10),Point(3,4)]))
print(compare([Point(2,3),Point(12,30),Point(40,50),Point(5,1),Point(12,10),Point(3,4)]))       