class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ml = 0 
        mr = len(numbers)-1
        l = numbers[ml]
        r = numbers[mr]
        while l<=r:
            if l+r == target:
                return [ml+1,mr+1]
            if l+r > target:
                mr -= 1
                r = numbers[mr]
            if l+r < target:
                ml += 1
                l = numbers[ml]
            

                