# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            #since setting each time, in order for this one to be balanced, not only are the heights 1 or less apart, but could have cases where are 1 or less apart overall, but below are not balanced, so need to store that accordingly
             #hence the check of left[0] and right[0]
            #my sexy avoids all this by having nonlocal/pointer/array variable outside that only goes to false if more than one apart anywhere
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
