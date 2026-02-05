class Solution:
    def dfs1(self, i: int, j: int, n: int, m: int, vis: List[List[bool]], a: List[List[int]]) -> int:

        if i < 0 or i > n - 1 or j < 0 or j > m - 1:
            return 0
        if vis[i][j] or a[i][j] == 0:
            return 0

        vis[i][j] = True
        ls = []
        ls.append(self.dfs1(i + 1, j, n, m, vis, a))
        ls.append(self.dfs1(i, j + 1, n, m, vis, a))
        ls.append(self.dfs1(i - 1, j, n, m, vis, a))
        ls.append(self.dfs1(i, j - 1, n, m, vis, a))
        vis[i][j] = False
        return a[i][j] + max(ls)

    def getMaximumGold(self, a: List[List[int]]) -> int:
        n = len(a)
        m = len(a[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] > 0:
                    vis = [[False] * m for _ in range(n)]
                    # print(i,j,m,n,vis,a)
                    y = self.dfs1(i, j, n, m, vis, a)
                    ans = max(y, ans)
        return ans





