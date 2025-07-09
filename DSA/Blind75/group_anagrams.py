class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s1 in s:
            s2 = s1
            d["".join(sorted(s1))].append(s2)
        return list(d.values())



