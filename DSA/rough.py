

# a=[1,0,0,0,1]
# n=1 # T

# a=[1,0,0,1]
# n=1 # F

a=[0,0,0,0,0]
n=1


lena= len(a)

if a[0] == 0 and a[1] == 0:
    a[0] = 1
    n = n - 1

for i in range(1,lena-1):
    if a[i]==0 and a[i-1]==0 and a[i+1]==0:
        a[i]=1
        n=n-1
        if n==0:
            break
if a[lena-1]==0 and a[lena-2]==0:
    a[lena - 1] =1
    n=n-1
if n<=0:
    print("True")
else:
    print("False")

