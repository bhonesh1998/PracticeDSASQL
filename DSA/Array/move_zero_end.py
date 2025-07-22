#https://leetcode.com/problems/move-zeroes/
from typing import List

class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        l = 0
        r = l + 1
        n = len(a)
        while l <= r and r < n:
            if (a[l] == 0 and a[r] != 0):
                a[l], a[r] = a[r], a[l]
                l += 1
                r += 1
            elif a[l] != 0:
                l += 1
                r += 1
            elif a[r] == 0:
                r += 1

        """
        Do not return anything, modify nums in-place instead.
        """
