#T: O(mn) run through grid twice including first for loop but constant doesn't change
#M: O(mn) because of visited set
#smart part is that instead of going from land pieces to treasure (mn)^3, doing bfs from all treasure simultaneiously
#so, anything visited already has minimum distance applied to it, because doing in rounds, so don't visit or touch again

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

      #in other problems, have done with directions = [] and list the directions and do this logic through loop
      #but this is another way, where just put in a function to abstract away and then call function four times
        def addCell(r, c):
            #all the conditions that would mean we shouldn't mark as visited and assign a distance
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])
            #don't have to assign distance here because loop does it when popped
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)): #do in range, because do in rounds, is important for distance assignment
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
