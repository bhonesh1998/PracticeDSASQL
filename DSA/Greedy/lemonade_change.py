#https://leetcode.com/problems/lemonade-change/description/
from typing import List
class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        v5 = 0
        v10 = 0
        for i in range(len(b)):
            if b[i] == 5:
                v5 += 1
            elif b[i] == 10:
                if v5 > 0:
                    v10 += 1
                    v5 -= 1
                else:
                    return False
            else:
                if (v10 >= 1 and v5 >= 1):
                    v10 -= 1
                    v5 -= 1
                elif v5 >= 3:
                    v5 -= 3
                else:
                    return False

        return True











