#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        n = len(a)
        i = 0
        for j in range(1, n):
            if a[i] != a[j]:
                i += 1
                a[i] = a[j]
        return i + 1
