class Solution:
    def findMin(self, a: List[int]) -> int:
        l=0
        h=len(a)-1
        ans=float('inf')
        while l<=h:
            mid = (l+h)//2
            if a[l]<=a[mid]:
                ans = min(ans,a[l])
                l=mid+1
                 # left sorted
            else:
                ans = min(ans,a[mid])
                h = mid -1
        return ans


