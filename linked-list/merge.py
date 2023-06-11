# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # T: O(n) M: O(1)
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        #VERY SMART STRAT TO AVOID CHECKING IF FIRST AND ALL THAT GARBAGE
        #doing it this way is smart because can use default node as dummy node since in while loop set next immediately
        #this way, without anychecking, dummy.next will be first node which we can return later
        dummy = ListNode()
        
        #newList is ready and newHead is a pointer to first thing in newList
        newList = dummy

        ##while one of them has not hit end
        while (list1 and list2):
            if (list1.val <= list2.val):
                #set and then move to next
                newList.next = list1
                list1 = list1.next
            else:
                #set and then move to next
                newList.next = list2
                list2 = list2.next
            newList = newList.next

        #once get here, one of them is null, so check which one and then append other
        if (not list1):
            newList.next = list2
        else:
            newList.next = list1

        return dummy.next
