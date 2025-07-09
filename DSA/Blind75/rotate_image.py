class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        m = len(a)
        n = len(a[0])
        for i in range(m):
            for j in range(i):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        for i in range(m):
            for j in range(n // 2):
                a[i][j], a[i][n - 1 - j] = a[i][n - 1 - j], a[i][j]
        return a

