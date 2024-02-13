def Pairs(open,close):
    if open=="[" and close=="]":
        return True
    if open=="{" and close=="}":
        return True
    if open=="(" and close==")":
        return True
    return False
def Balanced(ex):
    stack=[]
    for i in range(len(ex)):
        if ex[i]=="(" or ex[i]=="[" or ex[i]=="{":
            stack.append(ex[i])
        elif ex[i]==")" or ex[i]=="]" or ex[i]=="}":
            if Pairs(stack[-1],ex[i]):
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False
ex="({[]}){"
r=Balanced(ex)
if r==True:
    print("expresstion is Balanced")
else:
    print("expresstion is not Balanced")