# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#T: O(|p| + |q|) M: O(|p| + |q|)
#could use same conditions as did in iterative
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """handled in while loop
        #if both null, then are same
        if not p and not q:
            return True
        #if both aren't null, but one is, then are not same
        elif not p or not q:
            return False"""

        if not p and not q:
            return True

        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        else:
            #they are different
            return False

            




