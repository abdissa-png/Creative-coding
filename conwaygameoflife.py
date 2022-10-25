import copy
def conway(M,generations):
    printConway(M)
    for k in range(generations):
        future=[[0 for i in range(len(M[0]))] for j in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                future=checkConditions(future,M,i,j,len(M),len(M[0]))
        printConway(future)
        M=copy.deepcopy(future)
def checkConditions(Future,Matrix,rowi,columnj,row,column):
    count=0
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            if i==0 and j==0:
                continue
            else:
                if (columnj+j)>=0 and (columnj+j)<len(Matrix[0]) and (rowi+i)>=0 and (rowi+i)<len(Matrix):
                    if Matrix[rowi+i][columnj+j]==1:
                        count+=1
    if Matrix[rowi][columnj]==1 and count<2:
        Future[rowi][columnj]=0
    elif Matrix[rowi][columnj]==1 and (count==2 or count==3):
        Future[rowi][columnj]=1
    elif Matrix[rowi][columnj]==1 and (count>3):
        Future[rowi][columnj]=0
    elif Matrix[rowi][columnj]==0 and (count==3):
        Future[rowi][columnj]=1
    return Future
def printConway(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j]==0:
                print("0",end="  ")
            else:
                print("l",end="  ")
        print("\n")
    for i in range(80):
        print("-",end="")
    print("\n")
conway([[1,0,1,1],[1,1,0,0],[1,1,0,1],[0,1,1,0],[0,0,0,0]],8)