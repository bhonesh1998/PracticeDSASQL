
def enqueue(ls,x):
    ls.append(x)

def dequeue(ls):
    return ls.pop(0)

ls = []
print(ls)
enqueue(ls,1)
print(ls)
enqueue(ls,2)
print(ls)
print(dequeue(ls))
print(ls)
enqueue(ls,4)
print(ls)
print(dequeue(ls))
print(ls)