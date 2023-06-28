class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        #s is the string so far
        #num is the number of open parens
        #using recursive stack to be cracked
        #this is a backtracking problem, beacuse we're trying option on (adding open paren) and then undoing it/doing option 2
        #could use stack outside and then in each for loop append and then pop instead of passing string if you wanted but that's stupid
        def backtrack(s, numOpen, numClose):

            #base case is when fully formed
            if len(s) == 2 * n:
                result.append(s)
            if numOpen < n:
                backtrack(s + "(", numOpen + 1, numClose)
            if numClose < numOpen:
                backtrack(s + ")", numOpen, numClose + 1)
        
        backtrack("(", 1, 0)
        return result
