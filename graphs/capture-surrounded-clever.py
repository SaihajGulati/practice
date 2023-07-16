class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ###Reverse Thniking: capture all except for unsurrounded, instead of capture surrounded#
        #T: O(mn) M: O(1) average which is cracked, but worst could be O(mn) bc of recursive stack for capture

        
        ROWS, COLS = len(board), len(board[0])

        def markT(r, c):
            #if go out of bounds, or end up at X or T
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            markT(r + 1, c)
            markT(r - 1, c)
            markT(r, c + 1)
            markT(r, c - 1)

        # 1. (DFS) Temporarily mark unsurrounded regions (O -> T)
        #BC IT'S DFS, this goes through entire region if is not surrounded and marks as such
        for r in range(ROWS):
            for c in range(COLS):
                #means this is on one of the edges
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    markT(r, c)

        #2. the Os that are left are part of regions that are surrounded bc not marked t by above
        #capture rest (all that is left are surrounded)

        #could do both in this loop
        #tho it's not even be an optimization as if statement added here vs not before 
        #so kinda same (as long as change Os to Xs first, works bc this loop only sees each index once)
        #and other way is clearer and safer so that's better
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                """
                elif board[r][c] == "T":
                    board[r][c] = "O"
                """

        #3. the Ts need to be changed back to Os
        #change the unsurrounded areas back from their temp state
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
