class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # T: O(mn)
        # M: O(1)
        # this way below is slower than mine bc of fof if statement check each time in loop instead of doing first row seperately first which is no extra work
        #and that way doesn't even go through first row fully either which saves time
        #also this code ends up going through all and then checking if need to zero at end, while min only goes through columns and rows have to
        
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
