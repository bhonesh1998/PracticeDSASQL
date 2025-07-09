
'''
https://leetcode.com/problems/two-sum/
TC - O(N)
SC - O(N) FOR HASH TABLE

it can be solved using two pointer also but will take NlogN time - sorting

'''


from typing import List
class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(a)):
            dic[a[i]] = i
        for j in range(len(a)):
            if (target-a[j]) in dic.keys() and dic[target-a[j]]!=j:
                return ( [j, dic[target - a[j]]] )


obj = Solution()
x=obj.twoSum([1,2],3)
print(x)