# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        
        #find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next       

        #reverse time for second half
        #start at middle if odd length, or one past if even length
        curr = slow.next
        #prev meeds to be none so that end of reversed list is None
        #setting slow.next to None here is so that from front, list ends after half or one less than half
        #means in loop that merges, curr at end will end up properly noneing end because goes until back and sets back's next to tempLeft whiich will be none for that last one
        #in future can think of it as one side needs to include that one and other side can end before it
        prev = slow.next = None
        while curr:
            temp = curr.next
            #make this one attached to last one we saw
            curr.next = prev
            prev = curr
            #curr is moved one up
            curr = temp

        #merge time of two halves
        #slow is last one will need to attach to
        #now merge, only need to go up to and incl slow
        #curr starting with left one
        left = head
        #prev is the last value seen when reversing, so start of reversed list
        back = prev
        #we go until end of reversed list, which is either the middle element or one past middle if even length
        while back:
            tempLeft, tempRight = left.next, back.next

            #next one is now from the back
            left.next = back
            
            #next of back becomes next from left
            back.next = tempLeft

             #back is now the old next of it, and curr is now the old next of it
            back, left = tempRight, tempLeft

        return head
        
