from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = Counter(s)
        ts= Counter(t)
        return ss==ts