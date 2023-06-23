class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        #need to set down here because will changed always but starting here
        #by setting to n vs n-1, save cases where n-1 = 0 and have to add if statements that slow code
        #also in big scheme of things, n vs n-1 size down vs two if statements chekcs at the start evens out tbh
        down = [1] * n
        
        #order of this does not have to be reversed as never access m, but have to do m-1 times
        for i in range(m - 1): 
            #set each time to 1 because this represents right and will always start with one in rightmost
            #don't need array here because will only need one to right and then shifts
            right = 1
            for j in reversed(range(n-1)):
                #value for this gets stored in down for next time
                down[j] = right + down[j]
                #becomes right for this too for now
                right = down[j]
        
        #last one will be 0, 0 and both right and down[0] will be answer, and set down before so for 1 case, return down[0]
        return down[0]
