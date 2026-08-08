from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0: return False
        arr = Counter(nums)
        a,c =Counter.most_common(arr)[0]
        if c > 1:
            return True
        else:
            return False