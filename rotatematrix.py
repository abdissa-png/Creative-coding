def clockwise(M):
    m=len(M)
    printMatrix(M)
    n=len(M[0])
    i,j=m,n
    k,l=0,0
    while(i>1 and j>1):
        prev=M[k][l]
        for ind in range(j-1):
            curr=M[k][l+ind+1]
            M[k][l+ind+1]=prev
            prev=curr
        for ind in range(i-1):
            curr=M[k+ind+1][l+j-1]
            M[k+ind+1][l+j-1]=prev
            prev=curr
        for ind in range(j-1):
            curr=M[k+i-1][l+j-2-ind]
            M[k+i-1][l+j-2-ind]=prev
            prev=curr
        for ind in range(i-1):
            curr=M[k+i-2-ind][l]
            M[k+i-2-ind][l]=prev
            prev=curr
        k+=1
        l+=1
        i-=2
        j-=2
        #print(M,i,j,l,k)
    printMatrix(M)
#Clockwise 90 degree

def anticlockwise90(M):
    printMatrix(M)
    column=len(M[0])
    row=len(M)
    start1,start2=0,0
    while(row>1 and column>1):
        for index in range(column-1):
            M[start1][start2+index],M[start1+index][start2+column-1],M[start1+row-1][start2+column-1-index],M[start1+row-1-index][start2]=M[start1+index][column-1+start2],M[start1+row-1][start2+column-1-index],M[start1+row-1-index][start2],M[start1][start2+index]
        row-=2
        column-=2
        start1+=1
        start2+=1
    printMatrix(M)
def printMatrix(M):
    for row in M:
        for i in range(len(row)):
            print(row[i],end="   ")
        print("\n")
    for i in range(60):
        print("-",end="")
    print("\n")
def rotate180(M):
    printMatrix(M)
    for row in M:
        row.reverse()
    M.reverse()
    printMatrix(M)

matrix=[[1,2],[3,4]]
matrix1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]
matrix3=[[1,2,3],[4,5,6]]
matrix4=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix5=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
matrix6=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#(clockwise(matrix1))
#(clockwise(matrix2))
#(clockwise(matrix))
#(clockwise(matrix3))
#(clockwise(matrix4))
#(clockwise(matrix5))
#anticlockwise90(matrix)
#anticlockwise90(matrix2)
#anticlockwise90(matrix1)
#anticlockwise90(matrix6)
rotate180(matrix)
rotate180(matrix2)
rotate180(matrix1)
rotate180(matrix6)