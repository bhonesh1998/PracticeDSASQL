
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        n = len(a)
        s = [1] * n
        s[n - 1] = a[n - 1]
        for i in range(n - 1, 0, -1):
            s[i - 1] = a[i - 1] * s[i]
        p = 1
        ls = []
        for i in range(0, n):
            if i == n - 1:
                ls.append(p)
            else:
                ans = p * s[i + 1]
                p = p * a[i]
                ls.append(ans)
        return ls



