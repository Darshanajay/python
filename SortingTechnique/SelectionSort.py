def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
#        arr[i],arr[min] = arr[min],arr[i]
        t = arr[min]
        arr[min]=a[i]
        a[i]=t
a = [7, 9, 2, 6, 5, 3]
selection_sort(a)
print(a)