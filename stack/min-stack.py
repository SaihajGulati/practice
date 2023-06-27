class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        #min function, and conditional expression, and -1 for index of last
        #min stack of min value each time push, so when pop have correct min value each time as you cannot pop more than push
        minStackValue = min(val, self.minStack[-1]) if self.minStack else val
        self.minStack.append(minStackValue)


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()    

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
