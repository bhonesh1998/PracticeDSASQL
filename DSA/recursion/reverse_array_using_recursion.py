def f(a,i,j):
    if i<j:
        a[i],a[j]=a[j],a[i]
        return f(a,i+1,j-1)
    return

a=[1,2,3,4,5]
n=len(a)
f(a,0,n-1)
print(a)





