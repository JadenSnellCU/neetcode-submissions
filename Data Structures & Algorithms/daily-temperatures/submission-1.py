class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(t)):
            current_temp = t[i]
            while len(stack)!=0 and current_temp > stack[-1][0]:
                p = stack[-1][1]
                result[p] = i - p
                stack.pop()
            stack.append([t[i],i])
               
        return result