class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info = []
        fleets =[]
        for i in range(len(position)):
            info.append([position[i],speed[i]])
        info = sorted(info,key=lambda x: x[0], reverse =True)
        count = 0
        t = [target]*len(speed)
        cspd = info[-1][1]
        fleet_time = 0
        for i in range(len(speed)):
            ti = (target-info[i][0])/info[i][1]
            if ti <= fleet_time:
                continue
            else:
                fleet_time = ti
                count+=1
        return count