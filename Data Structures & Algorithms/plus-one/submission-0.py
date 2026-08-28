class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = digits[::-1]
        fin = []
        num = 0
        for i in range(len(a)):
            val = (10**i)*a[i]
            num+= val
        num +=1
        ns = str(num)
        for char in ns:
            n = int(char)
            fin.append(n)
        return fin