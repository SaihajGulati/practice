# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #T: O(n) M: O(1) bc only have one thing in memory, which is maxL
        #if asked to do this without referenced variable outside, could do with two values in array returned each time
        #then would be like isBalanced problem, where at bottom call return dfs(root)[0] which would be max diameter
        
        #in python arrays are automatically accessible nonlocally by nested function so wouldn't even have to pass like this
        def dfs(curr, maxLength):
            #gotta do a while loop
            if not curr:
                #-2 so that when get past end and add 2, get to 0 for length at that spot
                return 0

            #get max length going down on each side
            left = dfs(curr.left, maxLength)
            right = dfs(curr.right, maxLength)

            #left + right is diameter because height on each side includes between curr.left and curr and bw curr.right and curr
            maxLength[0] = max(left + right, maxLength[0])

            #because need to build up to calculate max height at each spot
            return 1 + max(left, right)
          
        #would be possibly a reference in another language or could do with an array like this
        maxL = [0]
        dfs(root, maxL)
        return maxL[0]
