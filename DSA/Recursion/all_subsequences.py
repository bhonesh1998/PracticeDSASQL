

def f(a,ind,ans):
    if ind>=len(a):
        print(ans)
        return
    ans.append(a[ind])
    f(a,ind+1,ans)
    ans.remove(a[ind])
    f(a,ind+1,ans)


ans = []
a=[3,2,1]
f(a,0,[])


