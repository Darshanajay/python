def Pairs(open,clcse):
    if open =="(" and clcse ==")":
        return True
    if open =="{" and clcse =="}":
        return True
    if open =="[" and clcse =="]":
        return True
    return False
def Bal(e):
    stack=[]
    for i in range(len(e)):
        if e[i]=="(" or e[i]=="{" or e[i]=="[":
            stack.append(e[i])
        elif e[i]==")" or e[i]=="}" or e[i]=="]":
            if Pairs(stack[-1],e[i]):
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False
e="{([])}{"
r=Bal(e)
if r==True:
    print("Balanced")
else:
    print("not Balanced")