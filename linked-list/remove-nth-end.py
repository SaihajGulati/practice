class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #T: O(n) but really O(n) not 2n like other way, hence why it's better M: O(1)
        #dummy, genius for reasons seen below
        #avoids weird if statement logic had to have in other way
        dummy = ListNode(0, head)
        left = dummy
        right = head

        #moves to next n times, so right ends up being n+1th node to right
        #so if n is length of list, then right ends up off
        #next while loop will never enter, and left will stay dummy
        #which is what we want so that left can connect to one it's supposed to without issue and checking if head specially
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

        #bc is dummy at start
        return dummy.next
