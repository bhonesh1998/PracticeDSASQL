class Solution:
    def maxProduct(self, a: List[int]) -> int:
        n=len(a)
        pr=1
        sx=1
        ans=float('-inf')
        for i in range(n):
            if pr==0:
                pr=1
            if sx==0:
                sx=1
            pr=pr*a[i]
            sx=sx*a[n-i-1]
            ans=max(ans,max(sx,pr))
        return ans


