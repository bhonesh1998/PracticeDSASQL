def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
def lcm(a,b):
    return (a*b)//gcd(a,b)

a,b = map(int,input().split())
print("gcd is {} , lcm is {} ".format(gcd(a,b),lcm(a,b)))

'''
OUTPUT :

2 5
gcd is 1 , lcm is 10 
'''


import math
print(math.gcd(a,b))


