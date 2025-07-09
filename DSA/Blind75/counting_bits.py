class Solution:

    def helper(self,n:int):
        if n==0:
            return 0
        return (n&1) + self.helper(n>>1)

    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            ans.append(self.helper(i))
        return ans
