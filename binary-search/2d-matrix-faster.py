class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        s = 0
        e = len(matrix) - 1
        row = -1
        ##this is for finding row
        ## check last ones to see if in between
        while (s <= e):
            m = int((s+e)/2)
            
            ##smart if statement setup to do less array checks
            ##if is first row, can't check one before
            if (matrix[m][0] > target):
                e = m - 1
            #this row is too small
            elif (matrix[m][-1] < target):
                s = m + 1
            #is in the row
            else:
                row = m
                break
        if (row == -1):
            return False
        l = 0
        r = len(matrix[row]) - 1
        
        while (l <= r):
            m = int((l+r)/2)
            if (matrix[row][m] > target):
                r = m - 1
            elif (matrix[row][m] < target):
                l = m + 1
            else:
                return True
        return False
