#min-heap
import math
class minheap:
    def __init__(self,capacity):
        self.storage=[None]*capacity
        self.capacity=capacity
        self.size=0
    def getParentIndex(self,index):
        return math.floor((index-1)/2)
    def getLeftChildIndex(self,index):
        return 2*index+1
    def getRightChildIndex(self,index):
        return 2*index+2
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index)<self.size
    def hasRightChild(self,index):
        return self.getRightChildIndex(index)<self.size
    def getParent(self,index):
        return self.storage[self.getParentIndex(index)]
    def getLeftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]
    def getRightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]
    def isFull(self):
        return self.capacity==self.size
    def swap(self,index1,index2):
        temp=self.storage[index1]
        self.storage[index1]=self.storage[index2]
        self.storage[index2]=temp
    def heapifyUp(self,index):
        if (self.hasParent(index) and self.getParent(index)>self.storage[index]):
            self.swap(self.getParentIndex(index),index)
            index=self.getParentIndex(index)
            self.heapifyUp(index)
    def insert(self,data):
        if self.isFull():
            raise Exception("Heap is full")
        self.storage[self.size]=data
        self.heapifyUp(self.size)
        self.size+=1
    def removeMin(self):
        if self.size==0:
            raise Exception("Empty heap")
        data=self.storage[0]
        self.storage[0]=self.storage[self.size-1]
        self.storage[self.size-1]=None
        self.size-=1
        self.heapifyDown()
        return data
    def heapifyDown(self):
        index=0
        while(self.hasLeftChild(index)):
            smallerChildIndex=self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.getRightChild(index)<self.getLeftChild(index)):
                smallerChildIndex=self.getRightChildIndex(index)
            if self.storage[index]<self.storage[smallerChildIndex]:
                break
            else:
                self.swap(index,smallerChildIndex)
                index=smallerChildIndex
class maxheap:
    def __init__(self,capacity):
        self.storage=[None]*capacity
        self.capacity=capacity
        self.size=0
    def getParentIndex(self,index):
        return math.floor((index-1)/2)
    def getLeftChildIndex(self,index):
        return 2*index+1
    def getRightChildIndex(self,index):
        return 2*index+2
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index)<self.size
    def hasRightChild(self,index):
        return self.getRightChildIndex(index)<self.size
    def getParent(self,index):
        return self.storage[self.getParentIndex(index)]
    def getLeftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]
    def getRightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]
    def isFull(self):
        return self.capacity==self.size
    def swap(self,index1,index2):
        temp=self.storage[index1]
        self.storage[index1]=self.storage[index2]
        self.storage[index2]=temp
    def heapifyUp(self,index):
        if (self.hasParent(index) and self.getParent(index)<self.storage[index]):
            self.swap(self.getParentIndex(index),index)
            index=self.getParentIndex(index)
            self.heapifyUp(index)
    def insert(self,data):
        if self.isFull():
            raise Exception("Heap is full")
        self.storage[self.size]=data
        self.heapifyUp(self.size)
        self.size+=1
    def removeMax(self):
        if self.size==0:
            raise Exception("Empty heap")
        data=self.storage[0]
        self.storage[0]=self.storage[self.size-1]
        self.storage[self.size-1]=None
        self.size-=1
        self.heapifyDown()
        return data
    def heapifyDown(self):
        index=0
        while(self.hasLeftChild(index)):
            GreaterChildIndex=self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.getRightChild(index)>self.getLeftChild(index)):
                GreaterChildIndex=self.getRightChildIndex(index)
            if self.storage[index]>self.storage[GreaterChildIndex]:
                break
            else:
                self.swap(index,GreaterChildIndex)
                index=GreaterChildIndex
def minheapsort(lst):
    heap=minheap(len(lst))
    for item in lst:
        heap.insert(item)
    for i in range(len(lst)):
        lst[i]=heap.removeMin()
    return(lst)
def maxheapsort(lst):
    heap=maxheap(len(lst))
    for item in lst:
        heap.insert(item)
    print(heap.storage)
    for i in range(1,len(lst)+1):
        lst[-i]=heap.removeMax()
    return(lst)
print(maxheapsort([24,63,71,89,-10,0,-6]))