from collections import Counter
s1="ab"
n = len(s1)
ls = list(s1)
c = Counter(ls)
print(c)
s2="eidbaooo"
for i in range(len(s2)-n+1):
    s=s2[i:i+n]
    c1=Counter(list(s))
    if c1==c:
        print("done")
        break

