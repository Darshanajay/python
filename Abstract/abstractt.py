class A:
    def __init__(self,tday,tmonth,tyear):
        self.day=tday
        self.month=tmonth
        self.year=tyear
    def show (self,showed):
        final=self.day,self.month,self.year
        print(final)
        print(showed)


Date=A(5,2,2024)
Date.show("over")