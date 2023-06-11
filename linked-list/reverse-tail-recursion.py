# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    #tail recursion because do work before recursion and simply return the recursive call
    #time: O(n) memory: 0(n) bc recursive stack
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        
        def reverseList(curr, prev):
            if (not curr):
                return prev

            temp = curr.next
            curr.next = prev

            #now gotta set for next
            #prev moves up to curr
            #curr moves up to temp
            return reverseList(temp, curr)
            
        return reverseList(head, None)
