def printMatrix(M):
    for row in M:
        for i in range(len(row)):
            print(row[i],end="   ")
        print("\n")
    for i in range(60):
        print("-",end="")
    print("\n")
def spiralMatrix(M):
    m=len(M)
    printMatrix(M)
    n=len(M[0])
    i,j=m,n
    k,l=0,0
    while(i>=1 and j>=1):
        if(i==1 or j==1):
            if i>1 and j==1:
                for ind in range(i):
                    print(M[k+ind][j],end=" ")
            elif j>1 and i==1:
                for ind in range(j):
                    print(M[k][l+ind],end=" ")
            else:
                print(M[k][l])
            k+=1
            l+=1
            i-=2
            j-=2
            break            
        for ind in range(j-1):
            print(M[k][l+ind],end=" ")
        for ind in range(i-1):
            print(M[k+ind][l+j-1],end=" ")   
        for ind in range(j-1):
            print(M[k+i-1][l+j-1-ind],end=" ")      
        for ind in range(i-1):
            print(M[k+i-1-ind][l],end=" ")
        if(i==1 or j==1):
            if i>1 and j==1:
                for ind in range(i):
                    print(M[k+ind][j],end=" ")
            elif j>1 and i==1:
                for ind in range(j):
                    print(M[k][j+ind],end=" ")
            else:
                print(M[k][l])
        k+=1
        l+=1
        i-=2
        j-=2
    print("\n")
spiralMatrix([[1,2,3],[4,5,6],[7,8,9]])
spiralMatrix([[1,2],[4,5]])
spiralMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
spiralMatrix([[1,2,3,4]])
spiralMatrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])