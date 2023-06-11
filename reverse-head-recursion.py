# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    ##head recursion, do recursion before work and notice how even return it
    #time: O(n) memory: 0(n) bc stack maintained
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        #check if not head as edge case if empty list, and other is actual base case as reach end of original and start of new
        if not head or not head.next: 
            return head
        
        #recurse forward
        newStart = self.reverseList(head.next)

        head.next.next = head
        ##needed so that at the end, when unpack recursion back up to first, the last node has its set appropiately set to None as it would be after reversing
        head.next = None
        
        return newStart
