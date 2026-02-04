

a=[10,22,12,3,0,6]
b=[]
mi = float('-inf')
for i in range(len(a)-1,-1,-1):
    if a[i]>mi:
        b.append(a[i])
        mi=a[i]
b.reverse()
print(b)
