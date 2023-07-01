# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        T: O(n) M: O(n)
        """
        curr = head
        nodes = []

        #until reach end of list
        #puts them all in the list
        while curr:
            nodes.append(curr)
            curr = curr.next

        #start one that is a dummy that can throw away, but useful to avoid checks
        dummy = ListNode()

        curr = dummy
        for i in range(0, (len(nodes)-1)//2 + 1):
            #temp for the left one
            left = nodes[i]
            #make the next one of list made so far stored in curr attached to left
            curr.next = left
            #make the next one of the left the one on the right
            left.next = nodes[-i-1]
            #update curr to be the list so far, which is next of left right now
            curr = left.next
        
        #with a case with odd length, last one will point to itself
        #at end, need to make next equal to none no matter list size even or odd, this works
        curr.next = None
