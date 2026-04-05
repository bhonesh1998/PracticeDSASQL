# https://leetcode.com/problems/assign-cookies/
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        lg=len(g)
        ls=len(s)
        g.sort()
        s.sort()
        gp=0
        sp=0
        while sp<ls and gp<lg:
            if g[gp]<=s[sp]:
                gp+=1
            sp+=1
        return gp