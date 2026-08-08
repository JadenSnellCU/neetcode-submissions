from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        g = {}
        f = []
        for s in strs:
            value = tuple(sorted(Counter(s).items()))
            if value not in g:
                g[value] = []
            g[value].append(s)
        f = list(g.values())
        return f