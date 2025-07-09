# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

n = int(input())
ls = Counter(list(map(int, input().split())))
q = int(input())
ans = 0
for i in range(q):
    x, y = map(int, input().split())
    if x in ls.keys() and ls[x] >= 1:
        ans += y
        ls[x] -= 1

print(ans)



