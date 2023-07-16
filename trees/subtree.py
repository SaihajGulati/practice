# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#T: O(n * m) bc does for each node in original tree (n) and each call at worst would have to check all of subtree (m)
#M: O(n) bc isSubtree maximum depth is size of tree (n). Even tho sameTree max stack is m where m is size of smaller of two trees (subtree), that is not kept after so at one time is max O(n+m), and m is smaller than n 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree1, tree2):
            if not tree1 and not tree2:
                return True
            elif tree1 and tree2 and tree1.val == tree2.val:
                return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
            #are different
            return False

        #need to handle here bc same tree will say false bc can't be "same" BUT we want true bc empty is subset of everything
        if not subRoot:
            return True

        #also check out here bc below calling root.left and right below
        #so helps avoid null issues
        elif not root:
            return False

        #check if the two trees rn are equal
        elif isSameTree(root, subRoot):
            return True

        #if not equal, need to check both sides down
        #need to check if is subtree, NOT SAME bc that only checks if next one is same, not if is subset of next batch down
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
