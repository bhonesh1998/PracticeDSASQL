

def f(a,i,n,su,ans):
    if i==n:
        ans.append(su)
        return
    f(a,i+1,n,su+a[i],ans) # pick
    f(a,i+1,n,su,ans) # not pick

ans=[]
a=[3,1,2]
f(a,0,len(a),0,ans)
ans=sorted(ans)
print(ans)