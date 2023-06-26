class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #l and r declared while t and b later
        #only declare in scope u need
        #will make moving easier too as only increment/decrement these and t and b will be fine
        l = 0
        r = len(matrix)-1
        #how many layers
        #not equal to, bc if last one is one in middle, then will be equal only, and then don't move
        while (l < r):
            t = l
            b = r
            #for each layer, need to do rotate process 1 less than length
            #r-l will be one less since is indexes
            for i in range(r-l):
                #save first one, which will put in at end
                #bc trick is to go backwards so don't need a trillion temps
                temp = matrix[t][l + i]
                
                #rotate process
                
                #move left column one to top row
                matrix[t][l + i] = matrix[b - i][l]
                
                #move bottom row one to left column
                matrix[b - i][l] = matrix[b][r - i]
                
                #move right column one to bottom row
                matrix[b][r - i] = matrix[t + i][r]
                
                #put in top row one into right column
                matrix[t + i][r] = temp
            l += 1
            r -= 1
