class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return []
        seen = {}
        for i in range(len(nums)):
            sum = target-nums[i]
            if(sum in seen and seen[sum]!=i):
                return [seen[sum],i]
            seen[nums[i]] = i
