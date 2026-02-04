from typing import List
class Solution:
    def maxSubArray(self, a: List[int]) -> int:

        n = len(a)
        dp = [0] * n
        if n == 1:
            dp[0] = a[0]
        elif n == 2:
            dp[0] = a[0]
            dp[1] = max(a[0], a[1], a[0] + a[1])
        else:
            dp[0] = a[0]
            dp[1] = max(a[0], a[1], a[0] + a[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], a[i] + dp[i - 1])
        return max(dp)


x=[1,2,3,-1,10]
obj = Solution()
print(obj.maxSubArray(x))