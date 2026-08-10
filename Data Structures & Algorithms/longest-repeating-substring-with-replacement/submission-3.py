from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==1:
            return 1
        elif len(s) == k:
            return k
        else:
            left = 0
            window = []
            count ={}
            mx =0
            for right in range(len(s)):
                if s[right] in count:
                    count[s[right]] += 1
                else:
                    count[s[right]] = 1
                window.append(s[right])
                while len(window)-max(count.values())> k:
                    window.remove(s[left])
                    count[s[left]]-=1
                    left +=1
                mx = max(mx,len(window))
            return mx

                

                

        