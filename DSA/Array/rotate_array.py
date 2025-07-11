#https://leetcode.com/problems/rotate-array/description/
from typing import List
class Solution:

    def re(self, a: List[int], l: int, r: int):
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

    def rotate(self, a: List[int], k: int) -> None:
        k = k % len(a)
        self.re(a, 0, len(a) - 1)
        self.re(a, 0, k - 1)
        self.re(a, k, len(a) - 1)

