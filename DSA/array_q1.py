n=int(input())
a=[]*n
for i in range(n):
    c=list(map(int,input().split()))
    a.append(c)
s1=s2=0
for i in range(n):
    for j in range(n):
        if i==j:
            s1+=a[i][j]
        if i+j==(n-1):
            print(i,j)
            s2+=a[i][j]
    print()
print(abs(s1-s2))