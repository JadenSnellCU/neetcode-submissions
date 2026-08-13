class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        elif len(piles)==1:
            return-(piles[0]//-h)
        else:
            l = 1
            r = max(piles)
            res =r
            while l <= r:
                mid = (l+r)//2
                t=0
                for i in range(len(piles)):
                    t += -(piles[i]//-mid)
                if t<=h:
                    res= mid
                    r = mid -1
                else:
                    l = mid + 1
            return res
                




        