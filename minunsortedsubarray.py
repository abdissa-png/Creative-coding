def minarray(arr):
    def findS(arr):
        for index in range(len(arr)-1):
            if arr[index]>arr[index+1]:
                return index
    def findE(arr):
        for index in range(1,len(arr)):
            if arr[-(index+1)]>arr[-index]:
                return len(arr)-index
    if findS(arr)==None:
        return "Array already sorted"
    s=findS(arr)
    e=findE(arr)
    Min=min(arr[s:e+1])
    Max=max(arr[s:e+1])
    for index in range(findS(arr)):
        if arr[index]>Min:
            s=index
            break
    for index in range(len(arr)-1,findE(arr),-1):
        if arr[index]<Max:
            e=index
            break
    return (arr[s:e+1],s,e)
print(minarray([10,12,20,30,25,40,32,31,35,50,60]))
print(minarray([0,1,15,25,6,7,30,40,50]))
print(minarray([0,1,15,30,40,50]))
    