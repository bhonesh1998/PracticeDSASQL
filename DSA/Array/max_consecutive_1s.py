# https://leetcode.com/problems/max-consecutive-ones/

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, a: List[int]) -> int:
        c = 0
        ans = 0
        for i in range(0, len(a)):
            if a[i] == 1:
                c += 1
                ans = max(ans, c)
            else:
                c = 0
        return ans
