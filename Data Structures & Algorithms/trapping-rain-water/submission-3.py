class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        prefix_max,suffix_max,water = [height[0]],[height[-1]],[0]*len(height)
        sm=0
        for i in range(1,len(height)):
            prefix_max.append(max(prefix_max[-1],height[i]))
        for i in range(len(height)-2,-1,-1):
            suffix_max.append(max(suffix_max[-1],height[i]))
        suffix_max.reverse()
        for i in range(len(height)):
            water[i] = min(prefix_max[i],suffix_max[i])-height[i]
            sm+= water[i]
        return sm
        
        
                    

            

            
            
        