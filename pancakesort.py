def pansort(arr,arr2=[]):
    if len(arr)<=1:
        return arr+arr2
    else:
        maxvalue=max(arr)
        index=arr.index(maxvalue)
        arr1=arr[:index+1]
        arr3=arr[(index+1):]
        arr1.reverse()
        arr4=arr1+arr3
        arr4.reverse()
        arr3=[arr4[-1]]
        return pansort(arr4[:len(arr4)-1],arr3+arr2)
#pansort based on better algorithm
def ceilSearch(arr,low,high,x):
    if x<=arr[low]:
        return low
    if x>arr[high]:
        return -1
    mid=(low+high)//2
    if(arr[mid]==x):
        return mid
    if(arr[mid]<x):
        if(mid+1<=high and x<=arr[mid+1]):
            return mid+1
        else:
            return ceilSearch(arr, mid+1, high, x)
    if(mid-1>=low and x>arr[mid-1]):
        return mid
    else:
        return ceilSearch(arr, low, mid-1, x)
def flip(arr,i):
    start=0
    while(start<i):
        temp=arr[start]
        arr[start]=arr[i]
        arr[i]=temp
        start+=1
        i-=1
def insertionSort(arr):
    for i in range(1,len(arr)):
        j=ceilSearch(arr, 0, i-1, arr[i])
        if j!=-1:
            flip(arr,j-1)
            flip(arr,i-1)
            flip(arr,i)
            flip(arr,j)
    return arr
print(pansort([23,10,20,11,12,6,7]))

print(insertionSort([18,40,35,12,30,35,20,6,90,80]))
