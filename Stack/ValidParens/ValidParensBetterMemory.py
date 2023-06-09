class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) % 2 == 1:
            return False

        stack  = []
        """
        makes code a lot shorter but if statements are faster runtime and less memory
        """
        parens = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                #needed check for nullness
                if len(stack) == 0:
                    return False
                # i returns what should be a closed parens type
                # stack pop returns an open parens type
                elif i == ")" and stack.pop() != "(":
                    return False
                elif i == "]" and stack.pop() != "[":
                    return False
                elif i == "}" and stack.pop() != "{":
                    return False   
        #if stack is empty, then all open parens have been hit by corresponding closed
        #and all closed had open hence why made it here
        #and correct order which stack ensures
        return len(stack) == 0
            
