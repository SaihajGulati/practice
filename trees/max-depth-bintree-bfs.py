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
    
        #iterative bfs
        if not root:
            return 0

        q = deque([root])
        level = 0

        while (q):

            #go through all at this level and add next level
            #python only checks the number that is the range once --> logical for this case and because otherwise would have to calculate it each time
            for i in range(len(q)):
                node = q.popleft()
                #don't need null check because will never add null node unlike dfs, and bc checked edge case before loop
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        return level
