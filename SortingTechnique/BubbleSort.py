a=[20,10,5,3]
for j in range(0,len(a)):
    for i in range(0,len(a)-j-1):
        if a[i]>a[i+1]:
            t = a[i]
            a[i] = a[i+1]
            a[i+1] = t
for j in range(0,len(a)):
    print(a[j])