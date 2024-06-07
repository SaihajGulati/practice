"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

#T: O(n) because is multiple of n (twice)
#M: O(n) extra with the hashmap (2n if include the new list, either way O(n))
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        #setting with None like this is key
        #handles both if 0 size list BUT ALSO easily accessing curr.next and curr.random in hashmap, which can be None
        oldToNew = {None: None}

        #first pass copying just the node value itself
        while curr: 
            node = Node(curr.val) #keeping null for next and random for now to save memory
            oldToNew[curr] = node
            curr = curr.next

        #second pass, updating the randoms and nexts
        #don't need second head because can just use hashmap
        curr = head
        while curr:
            newNode = oldToNew[curr]
            newNode.next = oldToNew[curr.next]
            newNode.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]
        
