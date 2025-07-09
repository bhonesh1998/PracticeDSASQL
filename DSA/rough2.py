
# 2n integers are given in array n is natural number , in array each element is positive
# parition array into n tuples in such a way that sum of minimum element from each tuple should be maximum.
# ex: a=[1,4,3,2]
# 1 + 3 = 4 , partitions :  (1,2) (3,4)

# n partitions

# a=[1,4,3,2]
# 1,2 3,4
# 1 + 3 = 4
#
# 2,4,5,10
# 2,5 4,10


a=[6,2,6,5,1,2]
#
# 2,1 2,5 6,6
#
# 1 + 2 + 6
ans=0
a.sort()
for i in range(len(a)):
    if i%2==0:
        ans+=(a[i])
print(ans)

