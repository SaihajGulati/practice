# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#T: O(n)
#M: O(n) or O(1) extra other than what is required by problem
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit = l1.val + l2.val
        head = ListNode(digit % 10)
        carry = 1 if digit > 9 else 0
        prev = head
        curr1, curr2 = l1.next, l2.next
        
        #have to worry about size difference
        while curr1 and curr2: 
            digit = curr1.val + curr2.val + carry
            carry = 0
            if digit > 9: 
                carry = 1  
                digit = digit % 10 
            node = ListNode(digit)
            prev.next = node
            prev = node
            curr1 = curr1.next
            curr2 = curr2.next

        #if curr1 is what's leftover
        while curr1:
            digit = curr1.val + carry
            carry = 0
            if digit > 9: 
                carry = 1  
                digit = digit % 10         
            node = ListNode(digit)
            prev.next = node
            prev = node
            curr1 = curr1.next
        
        while curr2:
            digit = curr2.val + carry
            carry = 0
            if digit > 9: 
                carry = 1  
                digit = digit % 10         
            node = ListNode(digit)
            prev.next = node
            prev = node
            curr2 = curr2.next

        #carry left at end
        if carry > 0: 
            node = ListNode(carry)
            prev.next = node

        return head


        
