def linearSearch(a,k):
    n=len(a)
    flag=False
    for i in range(0,n):
        if a[i] == k:
            flag=True
            break
    if flag:
        print("Given item is found",k)
    else:
        print("Given item is not found")
a=[5,1,4,2,8]
linearSearch(a,7)


