def search(l,k):
    f=0
    for i in range(0,len(l)):
        if l[i] == k:
            f=1
            break
    if f == 1:
        print("item found")
    else:
        print("item not found")
search([20,40,50,60,30,80],30)