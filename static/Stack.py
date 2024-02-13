class stack :
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values = [x]+self.values
    def pop(self):
        return self.values.pop(0)
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.values)
print(s.pop())
print(s.values)
print(s.pop())
print(s.values)
print(s.pop())
print(s.values)
print(s.pop())
print(s.values)
