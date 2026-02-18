from typing import List
class Solution:
    def maximumGap(self, a: List[int]) -> int:
        if len(a)<2:
            return 0
        else:
            a=sorted(a)
            m=-1
            for i in range(1,len(a)):
                m=max(m,a[i]-a[i-1])
            return m