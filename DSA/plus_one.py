class Solution:
    def plusOne(self, a: List[int]) -> List[int]:
        n = len(a)
        if a[n - 1] < 9:
            a[n - 1] = a[n - 1] + 1
            return a
        for i in range(n - 1, -1, -1):
            if i == 0 and a[i] == 9:
                a[i] = 0
                b = [1] + a
                print(b)
                return b
            elif a[i] < 9:
                a[i] = a[i] + 1
                return a
            else:
                a[i] = 0






