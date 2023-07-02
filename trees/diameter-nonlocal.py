# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(curr):
            nonlocal res
            if not curr:
                return 0

            #get both sides height
            left = dfs(curr.left)
            right = dfs(curr.right)

            #left + right is diameter because height on each side includes between curr.left and curr and bw curr.right and curr
            res = max(left + right, res)

            #because need to built up to calcuclate max height at each spot
            return 1 + max(left, right)
        
        dfs(root)
        return res
