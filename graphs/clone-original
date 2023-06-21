"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node
        #empty set so easy lookup in O(1)
        #T: O(N) and M: O(N)

        #acts as a visited too
        oldToNew = {}

        #n for node
        def dfs(v):
            
            #if get here, is not already visited so need to create new node and put in entry
            newNode = Node(v.val)
            oldToNew[v] = newNode
            
            #don't need stack as recursion does it
            #run recursion on each neighbor from new list
            #will end because only recurses sometimes, and should end with when get to node that has all neighbors already copied
            for n in v.neighbors:
                #if it's not in the list, then need to make copy of it so recurse to next level
                if not (n in oldToNew):
                    dfs(n)
                #add, whether it's one that had already been copied or one that was in recursion
                newNode.neighbors.append(oldToNew[n])
                
        dfs(node)
        return oldToNew[node]
