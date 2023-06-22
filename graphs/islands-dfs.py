class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            #have to check 0 here because is recursion and that is base case when stop recursing
            #since recursion, will be worse memory but otherwise same runtime as bfs
            if (r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit):
                return

            #this means is not any of those above things so is part of island
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                #just call it here as function handles end condition
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands
