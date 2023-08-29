# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    #resetting it each time instead of rightmost in queue bc you want last one that's actually real
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            
            #if did end up finding a rightSide at all, add it
            if rightSide:
                res.append(rightSide.val)
        return res
