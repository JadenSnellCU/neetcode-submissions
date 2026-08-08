class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        diff = []
        mn = 100
        mx = 0
        for i in range(len(prices)):
            mn = min(mn,prices[i])
            for j in range(i+1,len(prices)):
                mx = max(mn,prices[j])
                diff.append(mx-mn)
        return max(diff)