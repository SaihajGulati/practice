#T: O(nm) because in best case, do all work at first one, and then rest are stored so O(1) time, 
#opposite case all are same number or equally trash, then nm times do O(1) work
#M: O(nm)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cols = len(matrix[0])
        rows = len(matrix)
        #smarter to use hashmap for memo sometimes because saves some room if don't have n^2 to memoize
        #but here have to go through entire thing so just matrix is same
        memo = [[0]*cols for i in range(rows)] 

        def dfs(prev, r, c):
            #no visited needed, because is same check as if less than prev
            #smart way to check prev is with actual value instead of index
            if (
                r < 0 
                or r >= rows
                or c < 0
                or c >= cols
                or matrix[r][c] <= prev
            ):
                return 0

            if memo[r][c]: #nonzero, meaning know longest path from here
                return memo[r][c]

            currVal = matrix[r][c]

            #memoize here so that ones in this subtree can use
            #because imagine if one of this subtree's subtree is a subtree of another subtree
            #see drawing
            memo[r][c] = 1 + max(
                dfs(currVal, r + 1, c), 
                dfs(currVal, r - 1, c), 
                dfs(currVal, r, c + 1), 
                dfs(currVal, r, c - 1)
            )
            return memo[r][c]

        maxPath = 1
        #run through all options for start value
        for r in range(rows): 
            for c in range(cols): 
                #path is best path starting from rc
                #first time call, -1 as no values in matrix can be less than 0
                #storing max like this saves a tiny bit of time vs going through max at end
                maxPath = max(maxPath, dfs(-1, r, c))
        
        return maxPath




        
