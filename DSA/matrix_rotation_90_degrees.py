a=[[1,4,6],[8,9,7],[5,3,2]]
for i in range(len(a)):
    for j in range(i):
        a[i][j],a[j][i]=a[j][i],a[i][j]
print(a)
for i in range(len(a)):
    a[i].reverse()
print(a)