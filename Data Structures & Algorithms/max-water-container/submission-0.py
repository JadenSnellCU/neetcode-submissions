class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        l = 0
        r = len(heights)-1
        while l < r:
            d = r-l
            h = min(heights[l],heights[r])*d
            mx = max(h,mx)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        return mx

        