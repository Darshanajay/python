class Rectangle:
    def __init__(self,h,w):
        self.hight=h
        self.width=w
    def area(self):
        print(self.hight*self.width)
    def perimeter(self):
        print((self.hight+self.width)*2)
Rect=Rectangle(10,5)
Rect.area()
Rect.perimeter()