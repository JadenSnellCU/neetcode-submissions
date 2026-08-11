class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r = len(nums)-1

        while l <= r:
            mi = (r+l)//2
            if nums[mi]==target:
                return mi
            elif nums[mi] < target:
                l = mi+1
            else: 
                r=mi-1
        return -1
          
                

