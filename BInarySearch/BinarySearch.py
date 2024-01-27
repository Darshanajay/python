a=[3,7,9,16,25,28,30,35,40,42]
k=35
flag=False
lower=0
upper=len(a)-1
while lower <= upper:
    mid = lower+upper//2
    if a[mid] == k:
        flag =True
        break
    elif a[mid] > k:
        upper = mid-1
    else:
        lower=mid+1

if flag:
    print('item found')
else:
    print("item is not found")




