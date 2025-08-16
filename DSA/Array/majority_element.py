class Solution:

    def majorityElement(self, a: List[int]) -> int:
        c = 0
        n = len(a)
        ele = -1
        for i in range(n):
            if c == 0:
                ele = a[i]
                c += 1
            elif ele == a[i]:
                c += 1
            else:
                c -= 1
        cn = 0
        for i in range(n):
            if a[i] == ele:
                cn += 1
        if cn >= (n / 2):
            return ele




