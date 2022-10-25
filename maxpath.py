def printMatrix(M):
    for row in M:
        for i in range(len(row)):
            print(row[i],end="   ")
        print("\n")
    for i in range(60):
        print("-",end="")
    print("\n")
def maxPath(M):
    printMatrix(M)
    maxpathlist=[]
    j=M[0].index(max(M[0]))
    Max=max(M[0])
    maxpathlist.append(Max)
    for i in range(1,len(M)):
        if (j-1>0) and (j+1<len(M[0])) and (j<len(M[0])):
            greater=max(M[i][j-1],M[i][j+1],M[i][j])
            Max+=greater
            maxpathlist.append(greater)
            if greater==M[i][j-1]:
                j-=1
            elif greater==M[i][j+1]:
                j+=1
        elif (j-1>0) and (j+1<len(M[0])):
            greater=max(M[i][j-1],M[i][j+1])
            Max+=greater
            maxpathlist.append(greater)
            if greater==M[i][j-1]:
                j-=1
            elif greater==M[i][j+1]:
                j+=1
        elif (j+1<len(M[0])) and (j<len(M[0])):
            greater=max(M[i][j],M[i][j+1])
            Max+=greater
            maxpathlist.append(greater)
            if greater==M[i][j+1]:
                j+=1
        elif (j-1>0) and (j<len(M[0])):
            greater=max(M[i][j],M[i][j-1])
            Max+=greater
            maxpathlist.append(greater)
            if greater==M[i][j-1]:
                j-=1
    return Max,maxpathlist
print(maxPath([[10,10,2,0,20,4],[1,0,0,30,2,5],[0,10,4,0,2,0],[1,0,2,20,0,4]]))
print(maxPath([[1,2,3],[4,5,6],[7,8,9]]))