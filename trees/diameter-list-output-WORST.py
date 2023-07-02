# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #objectively worst memory wise compared to other solutions
        #T: O(V) M: O(2V) bc storing two for each
        def dfs(curr):
            #gotta do a while loop
            if not curr:
                #-2 so that when get past end and add 2, get to 0 for length at that spot
                return [0, 0]

            #get max length going down
            maxLeft, left = dfs(curr.left)
            maxRight, right = dfs(curr.right)

            #[max diameter, height]
            #compare new diameter with left and right, and max diameters seen in each subtree, 
            #which will ensure all maxes are being checked against each other by the time we recruse back to the top
            return [max(left + right, maxLeft, maxRight), 1 + max(left, right)]

      #return first value of output pushed up
        return dfs(root)[0]
