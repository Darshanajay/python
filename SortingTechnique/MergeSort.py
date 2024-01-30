def merge_sort(a):
    if len(a)>1:
        mid = len(a)//2
        left_side = a[:mid]
        right_side = a[mid:]
        merge_sort(left_side)
        merge_sort(right_side)
        i=j=k=0
        while i<len(left_side) and j<len(right_side):
            if left_side[i]<right_side[j]:
                a[k]=left_side[i]
                i=i+1
            else:
                a[k]=right_side[j]
                j=j+1
            k=k+1
            while i < len(left_side):
                a[k]=left_side[i]
                i=i+1
                k=k+1
            while j < len(right_side):
                a[k]=right_side[j]
                j=j+1
                k=k+1
a=[6,5,12,10,9,1]
merge_sort(a)
print("sorted list",a)