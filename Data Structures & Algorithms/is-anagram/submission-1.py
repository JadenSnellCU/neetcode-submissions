from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(Counter(s).most_common())==sorted(Counter(t).most_common())