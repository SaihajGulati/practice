# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#T: O(n)
#M: O(n) or O(1) extra compared to what is required of the problem
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #bloody genius way to avoid adding to empty list issue
        #can return dummy.next to get true head
        dummy = ListNode()
        prev = dummy

        carry = 0
        
        #the or carry also handles case where only carry left
        while l1 or l2 or carry: 
            #setting these separately is easy way to avoid length different adjusing later
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #compute new digit, doing // and % avoids if statement fluff
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            #make list
            prev.next = ListNode(val)

            #update pointers
            prev = prev.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next









        
