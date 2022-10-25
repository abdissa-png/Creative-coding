def printMatrix(M):
    for row in M:
        for i in range(len(row)):
            print(row[i],end="   ")
        print("\n")
    for i in range(60):
        print("-",end="")
    print("\n")
def matrixmultiplication(M,N):
    C=[]
    for i in range(len(M)):
        D=[]
        for j in range(len(N[0])):
            D.append(None)
        C.append(D)
    if len(M[0])==len(N):
        for i in range(len(M)):
            for j in range(len(N[0])):
                Sum=0
                for k in range(len(N)):
                    Sum+=(M[i][k]*N[k][j])
                C[i][j]=Sum
        return C
    else:
        return "Cant be multiplied"
matrix=[[1,2,3],[4,5,6]]
matrix1=[[1,2],[3,4],[5,6]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]
matrix3=[[10,11,12],[13,14,15],[16,17,18]]
printMatrix(matrixmultiplication(matrix,matrix1))
printMatrix(matrixmultiplication(matrix2,matrix3))