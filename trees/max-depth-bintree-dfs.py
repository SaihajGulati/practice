# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        #iterative pre-order dfs

        stack = [[root, 1]]
        maxDepth = 0
        #starting with maxDepth = 0 even though put 1 into stack is smart because then if root is null, return 0 we will never enter if statement
        #BUT by having 1 in the stack entry, you get the correct depth for each item in the stack in the likely case the root is not null

        while (stack):
            #can do this to get values from two elements from array-->ofc you can it's python!
            node, depth = stack.pop()

            if (node):
                maxDepth = max(maxDepth, depth)
                #append right first so that left is seen first (bc it's at top by being added second) in traditional pre-order dfs when pop from stack
                #is pre-order because notice how parent depth is checked before children's is
                #is dfs bc keep on prioritizing children
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])

        return maxDepth
