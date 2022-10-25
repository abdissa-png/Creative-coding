def freqsort(arr):
    arr1=[]
    for elem in arr:
        arr1.append(elem)
    arr1.sort()
    array=[]
    holder=[]
    for element in arr1:
        if len(holder)==0:
            holder.append(element)
        elif holder[0]!=element:
            array.append([holder[0],len(holder)])
            holder=[element]
        else:
            holder.append(element)
    array.append([holder[0],len(holder)])
    holder=[]
    maximum=array[0][1]
    for i in range(len(array)):
        for subarray in array:
            if subarray[1]>maximum:
                maximum=subarray[1]
                maxp=subarray
            elif subarray[1]==maximum:
                if arr.index(subarray[0])<arr.index(array[0][0]):
                    maximum=subarray[1]
                    maxp=subarray
        if maxp!=None:
            for i in range(maxp[1]):
                holder.append(maxp[0])
            array.remove(maxp)
            maxp=None
        else:
            if len(array)!=0:
                for i in range(array[0][1]):
                    holder.append(array[0][0])
                array.pop(0)
        if array!=[]:
            maximum=array[0][1]
    return holder
print(freqsort([2,5,2,6,-1,9999999,5,8,8,8]))
print(freqsort([2,5,2,8,5,6,8,8]))