class Conversion:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
        self.output=[]
        self.precedence={"+":1,"-":1,"*":2,"/":2,"^":3}
    def isEmpty(self):
        return self.top==-1
    def isfull(self):
        return self.top+1==self.capacity
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return
    def push(self,value):
        self.top+=1
        self.array.append(value)
    def isOperand(self,value):
        return value.isalpha()
    def notGreater(self,i):
        try:
            b=self.precedence[i]
            c=self.precedence[self.peek()]
            return True if c>=b else False
        except KeyError:
            return False
    def infixtopostfix(self,expr):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i=="(":
                self.push(i)
            elif i==")":
                while(not self.isEmpty() and self.peek()!="("):
                    self.output.append(self.pop())
                if (not self.isEmpty() and self.peek()=="("):
                    self.pop()
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        output=""
        for i in self.output:
            output+=i
        print(output)
    def postfixtoinfix(self,expr):
        for i in expr:
            if self.isOperand(i):
                self.array.insert(0,i)
            else:
                op1=self.array[0]
                self.array.pop(0)
                op2=self.array[0]
                self.array.pop(0)
                self.array.insert(0,"("+op2+i+op1+")")
            print(self.array[0])
if __name__=="__main__":
    exp="a+b*(c^d-e)^(f+g*h)-i"
    expr="abcd^e-fgh*+^*+i-"
    obj=Conversion(len(exp))

    obj.infixtopostfix(exp)
    obj.postfixtoinfix(expr)

