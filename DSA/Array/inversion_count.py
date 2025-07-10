# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

from typing import List
class Solution:
    def check(self, a: List[int]) -> bool:
        inc = 0
        n = len(a)
        for i in range(1, n):
            if a[i] < a[i - 1]:
                inc += 1
        if a[n - 1] > a[0]:
            inc += 1
        return inc<=1
