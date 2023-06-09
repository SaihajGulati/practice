class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) % 2 == 1:
            return False

        stack  = []
        parens = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for i in s:
            ##doing this with if statement saves runtime of getting all keys from above
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                #needed check for nullness
                if len(stack) == 0:
                    return False
                # i returns what should be a closed parens type
                # stack pop returns an open parens type
                ##using hashmap to do this makes code shorter and quicker as don't have to cycle through three if statements
                if (i != parens[stack.pop()]):
                    return False
        #if stack is empty, then all open parens have been hit by corresponding closed
        #and all closed had open hence why made it here
        #and correct order which stack ensures
        return len(stack) == 0
