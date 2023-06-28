class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #edge case written down bc of constraint giving this
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i in tokens:
            #don't have to do prechecks, because if isn't oeprator defined below, is a number by defintion
            #remember number 1 is older one, so two pops away
            #order only matters for sub and division
            #can't have append tracker, bc it just does operation to two most recent numbers, which could include answers
            if i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif i == '/': #is NOT floor but rather round toward 0, floor with negative makes more negative
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            elif i == '+':
                stack.append(int(stack.pop()+stack.pop()))
            else: #is just a number
                stack.append(int(i))
        return stack.pop()
