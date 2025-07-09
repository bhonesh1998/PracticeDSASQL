class Solution:
    def rob(self, a: List[int]) -> int:
        dp = []
        n = len(a)
        if n == 1:
            return a[0]
        elif n == 2:
            return max(a[0], a[1])
        else:
            dp.append(a[0])
            dp.append(max(a[0], a[1]))
            for i in range(2, n):
                dp.append(max(dp[i - 2] + a[i], dp[i - 1]))
            return dp[n - 1]
