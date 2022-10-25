class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def delete(self,data):
        if (data<self.data and self.left):
            self.left=self.left.delete(data)
        elif (data>self.data and self.right):
            self.right=self.right.delete(data)
        else:
            if(self.data==data):
                if (self.right and self.left):
                    """maxVal=self.left.findMax()
                       self.data=maxVal
                       self.left=self.left.delete(maxVal)"""
                    minVal=self.right.findMin()
                    self.data=minVal
                    self.right=self.right.delete(minVal)
                elif (self.left):
                    return self.left
                elif (self.right):
                    return self.right
                else:
                    return None
            return self
    def findMin(self):
        """ if self.left:
               return self.left.findMin()
            else:
                return self.data"""
        current=self
        while current.left:
            current=current.left
        return current.data
    def findMax(self):
        """if self.right:
              return self.right.findMax()
           else:
              return self.data"""
        current=self
        while current.right:
            current=current.right
        return current.data
    def find(self,data):
        if (data==self.data):
            return True
        elif (data<self.data and self.left!=None):
            return self.left.find(data)
        elif (data>self.data and self.right!=None):
            return self.right.find(data)
        else:
            return False
    def insert(self,data):
        if self.data==data:
            raise Exception("Data already exists")
        elif self.data>data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right=Node(data)
    def inorder(self,currentNode):
        if currentNode:
            self.inorder(currentNode.left)
            print(currentNode.data)
            self.inorder(currentNode.right)
    def preorder(self,currentNode):
        if currentNode:
            print(currentNode.data)
            self.preorder(currentNode.left)
            self.preorder(currentNode.right)
    def postorder(self,currentNode):
        if currentNode:
            self.postorder(currentNode.left)
            self.postorder(currentNode.right)
            print(currentNode.data)
    def height(self,currentNode):
        if currentNode==None:
            return -1
        leftHeight=self.height(currentNode.left)
        rightHeight=self.height(currentNode.Right)
        return max(leftHeight,rightHeight)+1
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root:
            self.root.insert(data)
        else:
            self.root=Node(data)
    def delete(self,data):
        if self.root:
            self.root=self.root.delete(data)
    def search(self,data):
        current=self.root
        while current!=None:
            if data<current.data:
                current=current.left
            elif data>current.data:
                current=current.right
            else:
                return True
        return False
    def find(self,data):
        if self.root:
            return self.root.find(data)
        return False
    def inorder(self):
        if self.root:
            self.root.inorder(self.root)
    def preorder(self):
        if self.root:
            self.root.preorder(self.root)
    def postorder(self):
        if self.root:
            self.root.postorder(self.root)
    def height(self):
        if self.root:
            return self.root.height(self.root)
        return -1
a=BST()
a.insert(50)
a.insert(25)
a.insert(75)
a.insert(15)
a.insert(35)
a.insert(65)
a.insert(85)
a.insert(10)
a.inorder()