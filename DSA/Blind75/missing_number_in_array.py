class Solution:
    def missingNumber(self, a: List[int]) -> int:
        x = 0
        y = 0
        for i in range(len(a)):
            x = x ^ a[i]
            y = y ^ i
        y = y ^ (i + 1)
        return x ^ y





