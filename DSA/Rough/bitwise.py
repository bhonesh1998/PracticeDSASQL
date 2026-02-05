import math

# bitwise ops
# & | ~ ^ << >>


x=int(input())
y=int(math.log2(x))
print(x,y)
if x==2**y:
    print('yes')
else:
    print('no')


print(2<<2) # left badega 2n
print(4>>2) # right kam hoga n/2

# odd even
if 5&1==1:
    print('o')
else:
    print('e')
