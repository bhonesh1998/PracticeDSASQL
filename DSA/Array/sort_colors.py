class Solution:
    def sortColors(self, a: List[int]) -> None:
        l = 0
        m = -1
        r = len(a) - 1
        while l <= r:
            if a[l] == 0:
                m += 1
                a[l], a[m] = a[m], a[l]
                l += 1
            elif a[l] == 2:
                a[l], a[r] = a[r], a[l]
                r -= 1
            else:
                l += 1








