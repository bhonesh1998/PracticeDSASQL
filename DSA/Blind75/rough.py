maxsum = float('-inf')
csum = 0
a=[-2,5,10,-2,20]
for i in range(len(a)):
    if csum<0:
        csum = 0
    csum = csum + a[i]
    maxsum=max(csum,maxsum)
print(maxsum)



