# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        #double reverse is the strat T: O(n)but really O(2n) M: O(1)
        
        #reverse until get to end
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #prev here is back
        second = prev
        prev = None
        #will end with second being one we want to remove and prev being one before it when going right to left (so one after it in normal ordering)
        for i in range(0, n-1):
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #this is the node to delete
        deleting = second

        #if not tryna delete first one and can therefore go more back
        if second.next:
            #this will make new second equal to left of deleting
            second = second.next
        else: #are deleting first, so need to make head equal to one right of it
            head = prev
        del deleting

        #reverse rest
        #now prev is still one right of deleted one
        #just second is one left of it, so can work appropiately
#reverse until get to end
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        return head
