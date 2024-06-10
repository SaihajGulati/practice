# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#T: O(n) where n is number of nodes, if were all on one side
#M: O(1)
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True: 
            if root.val > p.val and root.val > q.val: 
                root = root.left
            elif root.val < p.val and root.val < q.val: 
                root = root.right
            else: #is in between OR EQUAL to one of them, so is lowest common ancestor
                return root
      
