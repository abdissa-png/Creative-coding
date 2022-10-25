def mergesort(List):
    if len(List)<=1:
        return List
    elif len(List)>1:
        left=List[:len(List)//2]
        right=List[len(List)//2:]
        print(List)
        return merge(mergesort(left),mergesort(right),List)
def merge(list1,list2,list3):
    i,j,k=0,0,0
    while i<len(list1) and j<len(list2):
        if list1[i]>=list2[j]:
            list3[k]=list2[j]
            k+=1
            j+=1
        else:
            list3[k]=list1[i]
            k+=1
            i+=1
    while i<len(list1):
        list3[k]=list1[i]
        k+=1
        i+=1
    while j<len(list2):
        list3[k]=list2[j]
        k+=1
        j+=1
    return list3
print(mergesort([2,34,6,12,8,62,9,1,56,4,5234,34]))
