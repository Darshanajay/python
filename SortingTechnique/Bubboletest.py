def bubbloeSort(a):
    n=len(a)
    for i in range(0,n):
        for b in range(0,n-i-1):
            if a[b]>a[b+1]:
                t=a[b]
                a[b]=a[b+1]
                a[b+1]=t
a=[5,1,4,2,8]
bubbloeSort(a)
print(a)