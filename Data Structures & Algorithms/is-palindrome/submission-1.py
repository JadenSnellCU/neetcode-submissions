import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
        sx = cleaned[::-1]
        print(s)
        print(sx)
        return sx == cleaned
        