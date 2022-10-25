def dijsort(arr):
    low,mid,high=0,0,len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            mid+=1
            low+=1
            print(arr,low,mid,high)
        elif arr[mid]==1:
            mid+=1
            print(arr,low,mid,high)
        elif arr[mid]==2:
            arr[high],arr[mid]=arr[mid],arr[high]
            high=high-1
            print(arr,low,mid,high)
    return arr
print(dijsort([1,2,2,2,0,1,2,0,1,0,1,0,1]))