# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    #iterative
    #T: O(n) M: O(1) which is why best solution, because no lists or data structures and no recursive stack or anything to unpack or access
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        #until head.next does not point at null or nothing (better than while head because will need to return head so cannot be null at end)
        #psych nvm do it with head because this fixes empty case and then can use prev
        while head:
            #points to curr one looking at
            temp = head

            #head/curr moves on to original next
            head = head.next

            #the node looking at here is attached to the previous one, so new next
            temp.next = prev

            #prev moves to one looked at and changed here
            prev = temp

        #when get here, head.next is null, but head is not
        return prev
