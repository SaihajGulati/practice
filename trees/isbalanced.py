# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #like with diameter problem, could also do array of size 1 for holding True or False
        #could also do with if returned two values in an array, one being if balanced and other being height
        #then if statement would set the balanced to false if already false and true only if both sides show balanced and difference is 1 or less
        res = True
        def dfs(curr):
            nonlocal res
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            
            #will never be set to true, so if ends up false, means not balanced
            #this way avoids issue where have to set each time, which requires checking that none of the ones below were false, which would require an array returned of [balanced, height]
            if abs(left - right) > 1:
                res = False

            return 1 + max(left, right)

        dfs(root)
        return res
