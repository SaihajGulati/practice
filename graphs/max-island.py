class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0
        #method if can't rewrite original needs separate visited set
        #visited = set() 
        rows, cols = len(grid), len(grid[0])

        #T: O(mn) because going through all in for loop at bottom and for each island not visited run until end of island but mn dominates
        #S: O(mn) because will visited gets each one
        #could optimize a bit by writing over set by making all visited ones -1 for instance and but that makes S: O(mn)ish still because of recursive stack
        
        #goes to the end of an island
        def dfs(r, c):
            if (
                r < 0 
                or c < 0 
                or r == rows
                or c == cols
                or grid[r][c] != 1
                #or (r, c) in visited
            ):
                return 0

            #so that only starts new island if a part of it not seen yet
            grid[r][c] = -1 #way to show is visited, and if on top will catch with != 1
            #visited.append((r, c))

            #1 + ans because recurisvely building up from 0 answer at end when recurse off end to get size and need in all directions rest of island
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                #goes through all indexes, and calls dfs on each
                #in dfs, for each island not visited yet, visits it, gets size
                #if statement is done as base case up above
                #bfs finds size of this island
                maxIsland = max(maxIsland, dfs(r,c))

        return maxIsland
                
                





