class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if n == 0 or n == 1:
            return n
        else:
            dic = {}
            l = r = ans = 0
            while r < n:
                if s[r] in dic:
                    l = max(l, dic[s[r]] + 1)
                dic[s[r]] = r
                ans = max(ans, r - l + 1)
                r += 1
            return ans














