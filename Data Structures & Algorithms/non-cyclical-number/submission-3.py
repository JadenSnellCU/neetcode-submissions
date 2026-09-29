class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            ns = str(n)
            fin  = 0
            for s in ns:
                i = int(s)
                fin += i**2
            n=fin
            if n == 1:
                return True
            print(visit)
        return False
     
        