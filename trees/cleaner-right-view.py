# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#T: O(n) bc number of edges traveled which for tree is number of nodes minus 1
#M: O(n) bc the largest level  will be the largest queue situation, and that can be at most close to the size of the entire tree

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

            
        
