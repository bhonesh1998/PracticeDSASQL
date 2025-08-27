

def f(x):
    return x*x

def fun( fn, x1):
    return fn(x1)

print(fun(f,2))

ls = [1,2,3]

ls1=map(lambda x : x*2 , ls)

print([i for i in ls1])

print(str.__doc__)