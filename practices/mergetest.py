def mergeSort(a):
    if len(a)>1:
        mid=len(a)//2
        lefthalf=a[:mid]
        righthalf=a[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(a,lefthalf,righthalf)
def merge(a,lefthalf,righthalf):
    i=0
    j=0
    k=0
    while i<=len(lefthalf)-1 and j<=len(righthalf)-1:
        if lefthalf[i]<righthalf[j]:
            a[k]=lefthalf[i]
            i=i+1
            k=k+1
        else:
            a[k]=righthalf[j]
            j=j+1
            k=k+1

    if (i>len(lefthalf)-1):
        while j<= (len(righthalf)-1):
            a[k]=righthalf[j]
            j=j+1
            k=k+1
    else:
        while i<= (len(lefthalf)-1):
            a[k]=lefthalf[i]
            i=i+1
            k=k+1
a=[6,5,12,10,9,1]
mergeSort(a)
print(a)