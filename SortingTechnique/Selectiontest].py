def SelectionSort(a):
    n=len(a)
    for i in range (0,n):
        min = i
        for j in range(i+1,n):
            if a[min]>a[j]:
                min = j
        t=a[min]
        a[min]=a[i]
        a[i]=t
a=[5,1,4,2,8]
SelectionSort(a)
print(a)
