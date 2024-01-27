#a=[10,20,30,40,50]
def func (a,k):
    Flag = False
    for i in range(0,len(a)):
        if a[i]==k:
            Flag = True
            break
    if Flag == True:
        print("item found")
    else:
        print("item is not found")
func([10,20,30,40,50],40)