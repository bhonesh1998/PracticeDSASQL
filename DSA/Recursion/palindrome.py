def f(s,i,n):
    if i<n//2:
        if s[i]!=s[n-i-1]:
            return False
        return f(s,i+1,n)
    return True


s="cabbac"
print(f(s,0,len(s)))
