class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count = {}
        win_dict = {}
        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i],0)+1
        for right in range(len(s2)):
            win_dict[s2[right]]= win_dict.get(s2[right],0)+1
            while right-left+1 >len(s1):
                if win_dict[s2[left]] == 1:
                    del win_dict[s2[left]]
                else:
                    win_dict[s2[left]]= win_dict.get(s2[left])-1
                left+=1
            if count==win_dict:
                return True
            
        return False
        