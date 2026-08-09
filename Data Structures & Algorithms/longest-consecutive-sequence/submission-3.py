from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        c = sorted(Counter(nums))
        count = 1
        mx = 1
        for i in range(len(c)-1):
            if c[i]+1 == c[i+1]:
                count+=1
                mx = max(count,mx)
            else:
                count = 1
        return mx

        