class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = []
        for i in range(len(intervals)):
            n = len(ans)
            if len(ans) == 0 or (ans[n - 1][1] < intervals[i][0]):
                ans.append(intervals[i])
            else:
                ans[n - 1][1] = max(ans[n - 1][1], intervals[i][1])
        return ans

