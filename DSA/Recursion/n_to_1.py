

def f(i,n):
    if i<n:
        return
    print(i)
    return f(i-1,n)

f(10,1)