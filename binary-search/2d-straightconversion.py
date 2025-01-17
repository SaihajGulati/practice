class Solution:
    # Time Complexity: O(log(mn)) == O(logn + logm))
    # Space Complexity: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lnum = 0
        totalSize = len(matrix) * len(matrix[0])
        rnum = totalSize - 1
        cols = len(matrix[0])
        rows = len(matrix)

        while (lnum <= rnum):
            mnum = (lnum + rnum) // 2 #floor division to get middle value

            #convert
            mrow = mnum // cols
            mcol = mnum % cols

            curr = matrix[mrow][mcol]

            #found, return true
            if curr == target:
                return True
            #one in middle is bigger than target, need to look down as long as can
            elif curr > target:
                rnum = mnum - 1
            else: #don't need to check index valid because condition handles that
                lnum = mnum + 1
        
        return False







        
