class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack  = []
        parens = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for i in s:
            #bc only checks keys
            #if is an open one, want to add to stack
            #not in use is genius, but only if guaranteed to only get type of paren
            #otherwise checking if i == "(" or ... etc etc for all three is the way to go
            if i  not in parens:
                stack.append(i)
            #if get here, i is a closed parens type
            #if nothing in stack, is closed before next open, so false
            #if not equal, also false
            #this is why dictionary above needs to be setup with closing as key
            #not checks if empty, could also be len(stack) == 0
            elif not stack or stack.pop() != parens[i]:
                return False

        #if stack is empty, then all open parens have been hit by corresponding closed
        #and all closed had open hence why made it here
        #and correct order which stack ensures
        return not stack
