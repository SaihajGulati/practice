# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#T: O(n)
#M: O(n) bc number of edges traveled which for tree is number of nodes minus 1

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        result = []
        if root:
            q.append(root)

        while q: 
            #do this so you know you are sticking to one level
            #last one on this level will be seeable on right
            rowLen = len(q)
            for i in range(rowLen):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            #when get here, made it through row, and curr is rightmost of level
            result.append(curr.val)
        

        return result

            
        
