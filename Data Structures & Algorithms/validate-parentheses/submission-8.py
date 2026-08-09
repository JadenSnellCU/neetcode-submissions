class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack = []
        count = 0
        for char in s:
            if char in "([{":
                stack.append(char)
                count+=1
            else:
                print(stack)
                if len(stack) == 0:
                    return False
                if stack.pop() != pairs[char]:
                    return False
        if len(stack) != 0:
            return False
        return True

        