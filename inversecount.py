import random
def inversecount(arr):#time complexity O(n^2)
    count=0
    for i in range(0,len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                count+=1
    return count
class Node:
    def __init__(self,List,count=0):
        self.List=List
        self.count=count
def mergesort(a):
    if len(a.List)<=1:
        return a
    elif len(a.List)>1:
        left=Node(a.List[:len(a.List)//2])
        right=Node(a.List[len(a.List)//2:])
        return merge(mergesort(left),mergesort(right),a)
def merge(list1,list2,list3):
    i,j,k=0,0,0
    while i<len(list1.List) and j<len(list2.List):
        if list1.List[i]>list2.List[j]:
            list3.List[k]=list2.List[j]
            k+=1
            j+=1
            list3.count=list3.count+(len(list1.List)-i)
            #for ind in range(len(list1.List)-i):
                #print(list1.List[i+ind],list2.List[j-1])
        elif list1.List[i]==list2.List[j]:
            list3.List[k]=list1.List[i]
            k+=1
            i+=1
        else:
            list3.List[k]=list1.List[i]
            k+=1
            i+=1
    while i<len(list1.List):
        list3.List[k]=list1.List[i]
        k+=1
        i+=1
    while j<len(list2.List):
        list3.List[k]=list2.List[j]
        k+=1
        j+=1
    list3.count=list3.count+list1.count+list2.count
    #print(list1.List,list1.count,list2.List,list2.count,list3.List,list3.count)
    return list3
def invcount(arr):#nlog(N) time complexity
    a=Node(arr)
    c=mergesort(a)
    return c.count
array1=[]
for i in range(100):
    array1.append(random.randint(0,100))
#print(inversecount([1,20,6,4,5]))
#print(invcount([1,20,6,4,5]))
#print(inversecount([2,34,6,12,8,62,9,1,56,4,5234,34]))
#print(invcount([2,34,6,12,8,62,9,1,56,4,5234,34]))
print(invcount([1,20,6,22,5,4,5,5,4]))
print(inversecount([1,20,6,22,5,4,5,5,4]))
print(inversecount(array1),invcount(array1))
