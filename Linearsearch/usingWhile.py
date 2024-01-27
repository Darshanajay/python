def Search (l,k):
    i=0
    f=0
    while i<len(l):
        if l[i]==k:
            f=1
            break
        i = i + 1
    if f==1:
        print("item found ")
    else:
        print("item not found ")
Search([40,50,68,27,15,67,39],30)