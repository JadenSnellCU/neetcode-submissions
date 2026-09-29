from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = Counter(nums).most_common(k)
        ret = []
        for n,f in num:
            ret.append(n)
        return ret
