

def f(a,i,ans,k):
    if i>=len(a):
        if sum(ans)==k:
            print(ans)
        return
    ans.append(a[i])
    f(a,i+1,ans,k)
    ans.remove(a[i])
    f(a, i + 1, ans, k)


ans =[]
a=[3,2,1]

f(a,0,ans,3)
