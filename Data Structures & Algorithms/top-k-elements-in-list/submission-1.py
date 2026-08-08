from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = sorted(Counter(nums).most_common(k))
        d = []
        print(c)
        for i in range(len(c)):
            d.append(c[i][0])
        return d

        