class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #trick with this solution is that dp handles the relative order staying same as either right and down, or diagonal
        #suproblem is finding LCS of subset of both words
        #two cases though for relation depending on whether equal or not
        #C1: equal means add one to diagonal
        #if text1[i] = text2[j], then opt[i, j] = 1+opt[i+1,j+1]
        #C2: different means get max LCS of down and right
        #else, opt[i,j] = max(opt[i+1,j], opt[i,j+1])
        #need to solve all going up, so bottom up 

        #start with all zeros but remember length and height is one more than lengths, as this allows for full zero initialization because those outside zeroes will never be accessed
        #grid = [[0]*(len(text2) + 1) for i in range(len(text1) + 1)
        down = [0]*(len(text2) + 1) #can save memory by being smart and using only 1d array, bigger so diagonal can be 0 off end
        for i in reversed(range(len(text1))):
            #do need tracker for thisRow because otherwise diagonal would get overwritten
            #same thing where bigger so right can be 0
            #thisRow = [0]*(len(text2) + 1)

            #don't need a 2d array or any array at all for this as right one always switches to one just did and then diagonal needs to access down AND to right (diagonal) only once
            #so, if make tempcurr variable, then set down the diagonal one to old right, and then change right, works because
            #next iteration will be one j back, so will not access the down you just set as that is one right of diagonal of that now
            #set to zero as first right value is off end so always 0
            right = 0

            for j in reversed(range(len(text2))):
                curr = 0
                if text1[i] == text2[j]:
                    #if equal, then can add one and look at diagonal
                    #grid[i][j] = 1 + grid[i+1][j+1]
                    #thisRow[j] = 1 + down[j+1]
                    curr = 1 + down[j+1]
                    
                else:
                    #not equal so look at right and down
                    #grid[i][j] = max(grid[i][j+1], grid[i+1][j])
                    #thisRow[j] = max(down[j+1], down[j])
                    curr = max(right, down[j])
                #down and right becomes old right as when move up will need to be
                down[j+1] = right
                #right changes to curr so that next iteration is ready
                right = curr
            #0th index of down row never set since can't access at -1 so need to set here after do entire row
            down[0] = right
        return down[0]
