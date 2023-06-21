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
        #empty set so easy lookup in O(1)
        #T: O(N) and M: O(N)

        #acts as a visited too
        oldToNew = {}

        #this way now, return something with clear base case, and it is clearer in the for loop that you are creating connection to node returned
        #each call is an "attempt" to create a node
        def dfs(v):
            #means have already copied, so just return that copy instead of making new below
            if v in oldToNew:
                return oldToNew[v]
            
            #if get here, is not already visited so need to create new node and put in entry
            newNode = Node(v.val)
            oldToNew[v] = newNode
            
            #don't need stack as recursion does it
            #run recursion on each neighbor from new list
            for n in v.neighbors:
                #create connection to next node after "creating it"
                newNode.neighbors.append(dfs(n))
                
            return newNode

        #dfs(node) since called at the top and returns, will return start
        
        #mandatory null check
        return dfs(node) if node else None
