# https://leetcode.com/problems/bulb-switcher/?envType=problem-list-v2&envId=math
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0 or n==1:
            return n
        else:
            return math.floor(math.sqrt(n))