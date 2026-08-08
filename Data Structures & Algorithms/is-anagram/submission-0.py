from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = sorted(Counter(s).most_common())
        ct = sorted(Counter(t).most_common())
        return cs==ct