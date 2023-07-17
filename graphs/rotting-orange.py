class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #need bfs instead of dfs bc dfs will never let them meet in middle from each rotting one
        #bfs is made to go out in levels of a tree or graph
        q = collections.deque()
        fresh = 0
        time = 0

        #make the sources be the rotten ones and count fresh ones which will help at end
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        #queue popLeft means first in first out, so will go through ones at each level first before next level and so on and so forth
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        #needs this check bc you are removing from fresh as soon as see and only when see, BUT incrementing time everytime you enter while loop
        #so if only check is q is empty, on last one when only one fresh left in queue, will not find anymore fresh next to it to put in queue/rot but will still show that it took time (could also check if q is empty before incrementing time but that's lamer)
        #and fresh will be zero by then bc as soon as it's seen, it's made rotten
        
        while fresh > 0 and q:
            #need this inner for loop bc only want to increase time when completely empty this set from queue, as queue is all at same level
            #and putting the time incrementer outside the for loop but within a while loop iteration is the easiest way to do this
            #needed since one second is rotting all at one level away
            #range stores as variable so only takes len once
            for i in range(len(q)):
                r, c = q.popleft()

                #go in all directions and for every fresh see, make it rotton
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if this one next to us is in bounds and nonrotten, make rotten
                    # and add to q so can jump off from iit
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
