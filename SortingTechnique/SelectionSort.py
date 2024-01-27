a=[7,9,2,6,5,3]
for i in range(0,len(a)):
    min =  i
    for j in range(i+1,len(a)):
        if a[j]<a[min]:
            min=j
            t=a[min]
            a[min]=a[j]
            a[j]=t
for i in range(0,len(a)):
    print(a[j])

