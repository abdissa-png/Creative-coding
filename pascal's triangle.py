row=int(input("enter the number of rows:"))
def f(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
print(1,end="\n")
for i in range(1,row+1):
    c=0
    while c<=i:
        print(int((f(i))/((f(i-c))*f(c))),end=" ")
        c=c+1
    print(" ")
        
