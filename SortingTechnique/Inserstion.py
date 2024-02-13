a=[89,45,68,90,29,34,17]
def InsertionSort(a):
    n=len(a)
    for i in range(1,n):
        key = a[i]
        j=i-1
        while (j>=0 and a[j]>key):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
InsertionSort(a)
print(a)
