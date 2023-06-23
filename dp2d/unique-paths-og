class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1:
            return m
        elif n <= 1:
            return n
        #reversed range means goes 2, 1, 0 if m = 3 (starts from m-1 and includes 0)
        #below setup starts at rightbottom and then for each row moves left and then up
        #start with bottom row, get all ones in bottom row and rightmost ccolum always so can skip that row and column, so starting at 2nde rightmost of 2nd to last row, where right is 0 but down is 1
        #can do this as 0 case is checked above and so 1 case works with below and will just never enter for loop
        
        #need to set down here because will changed always but starting here
        down = [1] * (n-1)
        
        for i in reversed(range(m-1)):
            #set each time because is the same starting right for each row as last column is all 1s
            right = 1
            for j in reversed(range(n-1)):
                temp = right + down[j]
                #because this becomes new right, make right equal to temp
                right = temp
                #next time this j is used will be next row, so set down[j] to temp too
                down[j] = temp
        
        #last one will be 0, 0 and both right and down[0] will be answer, and set down before so for 1 case, return down[0]
        return down[0]
