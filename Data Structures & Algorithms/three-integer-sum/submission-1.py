class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        ml = 0
        mc = ml+1
        mr = len(sn)-1
        l = sn[ml]
        c = sn[mc]
        r = sn[mr]
        arr = []
        for i in range(len(sn)-2):
            if i > 0 and sn[i] == sn[i - 1]:
                continue
            ml = i
            mc = ml+1
            mr = len(sn)-1
            l = sn[ml]
            
            while mc < mr:
                c = sn[mc]
                r = sn[mr]
                if  l + c + r == 0:
                    arr.append([l,c,r])
                    mc +=1
                    mr -=1
                    while mc < mr and sn[mc] == sn[mc - 1]:
                        mc += 1
                elif l + c + r > 0:
                    mr -=1
                elif l + c + r < 0:
                    mc +=1
        return arr

        