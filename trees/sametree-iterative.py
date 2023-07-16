# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#T: O(|p| + |q|) M: O(|p| + |q|)
#way more complex to write it iteratively with no benefit, but sometimes there is and it's good to know
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """handled in while loop
        #if both null, then are same
        if not p and not q:
            return True
        #if both aren't null, but one is, then are not same
        elif not p or not q:
            return False"""

        pQ = deque([p])
        qQ = deque([q])
        
        while qQ and pQ:
            qNode = qQ.popleft()
            pNode = pQ.popleft()
            

            #if the values exist and are not same, return False
            if ((qNode and pNode) and (qNode.val != pNode.val)) or (qNode and not pNode):
                return False
            
            if qNode:
                qQ.append(qNode.left)
                qQ.append(qNode.right)
            if pNode:
                pQ.append(pNode.left)
                pQ.append(pNode.right)
        
        #if get here, one of them ran out
        #need to check that both are empty
        return not qQ and not pQ
            
