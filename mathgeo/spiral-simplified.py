class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #T: O(mn) 
        #Extra M: O(1) bc only output array is there which isn't extra
        res = []
        #start with the right and bottom out of bounds bc will go up to it but right before (exclusive end)
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row and then change top once used it up
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col and then move right back
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row and then move bottom up
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the left col and then move left up
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        #by starting with them out of bounds and thus exclusive on each side, and then moving the cocunters right after, means end is really easy
        return res
