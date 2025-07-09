# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, a: List[int]) -> int:
        i=0
        j=1
        ans=-1
        n=len(a)
        if n==1:
            return 0
        else:
            mi = a[0]
            for j in range(1,n):
                if a[j]>mi:
                    ans = max(ans,a[j]-mi)
                mi = min(mi,a[j])
        if ans==-1:
            return 0
        else:
            return ans