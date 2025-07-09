class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        dp = []
        dp.append(a[0])
        n = len(a)
        for i in range(1, n):
            dp.append(max(dp[i - 1] + a[i], a[i]))
        return max(dp)


