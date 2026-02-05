# https://leetcode.com/problems/gas-station/description/
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tg = sum(gas)
        tc = sum(cost)
        rg = 0
        ans = 0

        if tg < tc:
            return -1

        for i in range(n):
            rg += (gas[i] - cost[i])
            if rg < 0:
                ans = i + 1
                rg = 0
        return ans

# obj = Solution()
# print(obj.canCompleteCircuit([1,4,3],[2,2,3]))

