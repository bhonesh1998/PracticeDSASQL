class Solution:
    def canJump(self, a: List[int]) -> bool:
        n = len(a)
        mn = n - 1
        for i in range(n - 2, -1, -1):
            if (i + a[i]) >= mn:
                mn = i
        return mn == 0


