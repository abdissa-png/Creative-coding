#better than O(n^2) algorithm
def kdif(arr,k):
    arr.sort()
    Sum=0
    holder={}
    for element in arr:
        if element not in holder:
            holder[element]=1
        else:
            holder[element]+=1
    for i in range(len(arr)):
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if (arr[i])+k==arr[mid]:
                Sum+=holder[arr[mid]]
                break
            elif arr[i]+k<arr[mid]:
                high=mid-1
            else:
                low=mid+1
    return Sum,arr
print(kdif([1,3,5,8,6,4,6,6,10,8], 2))