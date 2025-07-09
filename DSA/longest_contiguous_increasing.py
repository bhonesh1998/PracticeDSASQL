class Solution:
    def findLengthOfLCIS(self, a: List[int]) -> int:
        if len(a) == 1:
            return 1
        i = 1
        cr = 1
        ans = 0
        while i < len(a):
            if a[i] > a[i - 1]:
                cr += 1
            else:
                cr = 1
            ans = max(ans, cr)
            i += 1

        return ans

