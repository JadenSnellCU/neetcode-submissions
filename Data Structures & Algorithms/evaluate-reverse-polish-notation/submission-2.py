class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = ['+','-','*','/']
        stack = []
        result = 0
        for i in range(len(tokens)):
            if tokens[i] not in arr:
                stack.append(int(tokens[i]))
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                if tokens[i] == '+':
                    z = x+y
                    result += z
                elif tokens[i] == '-':
                    z = y-x
                    result += z
                elif tokens[i] == '*':
                    z = x*y
                    result *= z
                else:
                    z = y/x
                stack.append(z)
        return int(stack[0])