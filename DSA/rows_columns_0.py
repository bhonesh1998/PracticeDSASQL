a=[

    [1,0,0],
    [2,0,4],
    [0,0,0]

]

rr = set()
cr = set()
r=len(a)
c=len(a[0])
for i in range(r):
    if all(a[i][j]==0 for j in range(c)):
        rr.add(i)
for j in range(c):
    if all(a[i][j]==0 for i in range(r)):
        cr.add(j)
ans=[]
for i in range(r):
    if i not in rr:
        nl=[a[i][j] for j in range(c) if j not in cr]
        ans.append(nl)

print(ans)