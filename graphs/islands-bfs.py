class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

        def bfs(r,c):
            #adds passed spot to start of q (so is start of search)
            #smart to use deque because do convert to dfs, all have to do is change popLeft below to pop(), 
#and that becomes dfs by jumping to last direction added each time which means goes to end of each branch instead of by level
#here dfs ends up basically doing same thing as bfs though as they are marked as visited when first seen/added to queue
            q = deque()
            visited.add((r,c))
            q.append((r,c))
        
            while q:
                row,col = q.popleft() #here could be pop for pseudo dfs
                directions= [[1,0],[-1,0],[0,1],[0,-1]]
            
            #this for loop giving dr dc like this so easily is crazy
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    #making sure is valid index, is land, and is not already visited so can add to queue to process
                    #since only adds to q if is 1, will stop once hits end of island
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                    
                        q.append((r , c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                #if get there, means is land have not seen yet and is not part of another island since bfs function goes until end of island
                #therefore, once bfs function ends, we can increment island count
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1 

        return islands
