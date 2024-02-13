class stack:
    s = []
    max = 5

    def isFull(self):
        if len(self.s) == max:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

    def spush(self):
        if self.isFull():
            print("stack is full")
        else:
            ele = int(input("enter a element"))
            self.s.append(ele)

    def spop(self):
        if self.isEmpty():
            print("under progress")
        else:
            ele = self.s.pop()
            print("poped element is ", ele)

    def disp(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            for i in range(len(self.s) - 1,-1,-1):
                print(self.s[i])

    def top(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("top element is", self.s[-1])


ss = stack()
while True:
    c = int(input("enter a choice 1:push 2:pop 3:disp 4:top 5:exit"))
    if c == 1:
        ss.spush()
    elif c == 2:
        ss.spop()
    elif c == 3:
        ss.disp()
    elif c == 4:
        ss.top()
    else:
        print("invalid choice")
        break
