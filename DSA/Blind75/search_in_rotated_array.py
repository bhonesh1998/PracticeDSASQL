class Solution:
    def search(self, a: List[int], target: int) -> int:
        n = len(a)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if a[m] == target:
                return m
            elif a[l] <= a[m]:
                if a[l] <= target and a[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            elif a[m] <= a[r]:
                if a[r] >= target and a[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
        return -1


