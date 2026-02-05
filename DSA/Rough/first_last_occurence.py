class Solution:
    def searchRange(self, a: List[int], t: int) -> List[int]:
        if len(a) == 1:
            return [0, 0] if t == a[0] else [-1, -1]
        l = 0
        h = len(a) - 1
        a1 = -1
        a2 = -1
        while l <= h:
            m = (l + h) // 2
            if t == a[m]:
                k = m
                p = m
                while k >= 0 and t == a[k]:
                    k -= 1
                a1 = k
                while p <= (len(a) - 1) and t == a[p]:
                    p += 1
                a2 = p
                return [a1 + 1, a2 - 1]
            elif t > a[m]:
                l = m + 1
            elif t < a[m]:
                h = m - 1
        return [a1, a2]





