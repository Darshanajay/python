class stack:
    s=[]
    maxsize=4

    def isFull(self):
        if len(self.s)==self.maxsize:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.s)==0:
            return True
        else:
            return False

    def spush(self):
        if self.isFull():
            print("stack is full")
        else:
            ele = int(input("Enter a ele"))
            self.s.append(ele)

    def spop(self):
        if self.isEmpty():
            print("stack under flow")
        else:
            ele=self.s.pop()
            print("poped element is",ele)

    def disp(self):
        if self.isEmpty():
            print("empty stack")
        else:
            for i in range(len(self.s)-1,-1,-1):
                print(self.s[i])

    def speek(self):
        if self.isEmpty():
            print("stack Empty")
        else:
            print("peek ele is ",self.s[-1])

s1=stack()
while True:
    c=int(input("enter a choice 1:push 2:pop 3:disp 4:peek 5:exit"))
    if c==1:
        s1.spush()
    elif c==2:
        s1.s.pop()
    elif c==3:
        s1.disp()
    elif c==4:
        s1.speek()
    else:
        print("invalid choice")
        break