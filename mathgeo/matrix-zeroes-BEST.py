class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # T: O((mn)
        # M: O(1)
        # this way below is faster than Neet bc of for loop at start instead of if statement check each time in loop
        #and bc only go through rows and columns needed with for loops at the end, while neet's code ends up going through all and then checking if need to zero

      
        #for first row (first cell in column data holder), use zeroth row variabled
        #set by default to nonzero value so that only have to set to zero for if this first row is needed to be all zeros bc encounter one
        zeroRow = False
        COLS = len(matrix[0])
        ROWS = len(matrix)
        
        #for 0th row
        for colIndex in range(COLS):
            if matrix[0][colIndex] == 0:
                zeroRow = True
                break #bc already know this row will be zeroed AND all others that affect their column, are already zero so no need to go through all and check   
        #go from 1 bc already did first row checking
        for rowIndex in range(1, ROWS):
            for colIndex in range(COLS):
                if matrix[rowIndex][colIndex] == 0:
                    #set top row to zero (this indicates which columns to zero out)
                    #the first column being zeroed out is why have to start at 0 for j
                    matrix[0][colIndex] = 0
                    #set left column value to zero (this indicates which rows to zero out)
                    matrix[rowIndex][0] = 0
        
        #do filling in rows with zeros:
        #have to do rows first, bc if do cols first, will overwrite first column which affects which rows get 0ed out
        #this one doesn't overwrite cols since we are starting from row 1
        #start at one again bc zeroth row variable is seperate
        for rowIndex in range(1, ROWS):
            if matrix[rowIndex][0] == 0:
                #fill in row with zeroes
                for colIndex in range(COLS):
                    matrix[rowIndex][colIndex] = 0

        #do filling in columns with zeroes
        for colIndex in range(COLS):
            if matrix[0][colIndex] == 0:
                #go down column and fill with zeroes
                #include first row
                for rowIndex in range(ROWS):
                    matrix[rowIndex][colIndex] = 0

        #now do for 0th row if is supposed to be zeroed out
        if zeroRow:
            for colIndex in range(COLS):
                matrix[0][colIndex] = 0
