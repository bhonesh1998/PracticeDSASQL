
a=[1,2,3,4,5]
b=[]

n=len(a)
k=1
for i in range(n):
    b.append(a[(i+k)%n])
print(b)