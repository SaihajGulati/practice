class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #T: O(n) but really O(n) not 2n like other way, hence why it's better M: O(1)
        #dummy, genius for reasons seen below
        #avoids weird if statement logic had to have in other way
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for i in range(n):
            right = right.next

        #move until right hits off end
        #we want left to be before so can connect to one after deletion one, hence dummy so don't have to worry about null situations before and weirdness
        #hence dummy
        while right:
            left = left.next
            right = right.next

        deleting = left.next
        left.next = deleting.next
        del deleting
        
        return dummy.next
