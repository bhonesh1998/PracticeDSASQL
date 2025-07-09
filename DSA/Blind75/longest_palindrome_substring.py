s="ababd"
n=5
for k in range(n):
    i=k
    j=k
    ans = s[k]
    while i>0 and j<n:
        i=i-1
        j=j+1
        if i>=0 and j<n and s[i]==s[j]:
            ans = s[i]+ans+s[j]
        else:
            break






