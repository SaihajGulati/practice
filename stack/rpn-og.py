class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #edge case written down bc of constraint giving this
        if len(tokens) == 1:
            return int(tokens[0])

        #T: O(n) bc is O(2n) M: O(n) similarly
        stack = []
        for i in tokens:
            #can't really check if is number, but can check if is operator by being smart
            #have to check if length is one so that can run ord
            if len(i) == 1 and ord(i) >= 42 and ord(i) <= 47:
                #if nothing, need to go back two numbers
                
                #don't check not ans, because will end up true when ans is 0
                #and that is big biff if end up with partial sum of 0
                
                #remember num1 is two pops away since it is from the back
                num2 = stack.pop()
                num1 = stack.pop()

                #can't have append tracker, bc it just does operation to two most recent numbers, which could include answers
                if i == '*':
                    stack.append(num1 * num2)
                elif i == '-':
                    stack.append(num1 - num2)
                elif i == '/': #is NOT floor but rather round toward 0, floor with negative makes more negative
                    stack.append(int(num1 / num2))
                elif i == '+':
                    stack.append(int(num1 + num2))
            else: #is just a number
                stack.append(int(i))
        return stack.pop()
