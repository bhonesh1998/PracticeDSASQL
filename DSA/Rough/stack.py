
def pop(ls):
    return ls.pop()

def push(ls,x):
    ls.append(x)

ls = []
print(ls)
push(ls,1)
print(ls)
push(ls,2)
print(ls)
print(pop(ls))
print(ls)
push(ls,4)
print(ls)
print(pop(ls))
print(ls)
