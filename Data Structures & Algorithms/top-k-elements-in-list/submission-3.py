from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cs = sorted(Counter(nums).most_common(k))
        return [c[0] for c in cs]

        