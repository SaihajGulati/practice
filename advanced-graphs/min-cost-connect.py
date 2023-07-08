class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #T: O(ElogE) because each time add to heap, log(number of stuff in heap) time --> can become O(ElogV) 
        #S: O(V + E) which is adjacency list bc V number of keys and each has it's edges number of elements so total is sum of v and e
        #since fully connected graph E = V^2, so space can cimplify to either O(E) or O(V^2) which is O(n^2)
        Ebecause in heap code below, since don't add if is already in tree, heap will have max one of each node which is V,
        #ElogV becomes n^2logn as edges from all edges to each other (n^2) and n is number of points/nodes
        #S:
        #literally MST, so can use Prim's or Reverse-Delete or Kryskall's
        
        #first make adjacency list that stores [cost, node]
        #need this so can easily choose minimum each time to connect to new node
        N = len(points) #number of points

        adj = {i : [] for i in range(N)} #starts with empty list for each i

        #each one has to have the distances for each of the other ones
        #O(E+V)
        for i in range(N):
            x1, y1 = points[i]
            #make sure is i+1 so don't just put same one in with 0 distance for no reason
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2-y1)
                #smartest to store by index so can access original array if needed and is just easier than tuple, and for this problem, we only need to return min cost not min tree or anything so don't have to worry about storing it
                #smartest to make dist first part of list so that can use heap to sort by that
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        #Prim's
        res = 0
        #set so can easily see if already put in or not
        #checking against this is how we avoid cycles
        tree = set()
        #minHeap of neighbors of nodes in tree (hence name minHN)
        #useful because minHeap sorts based on first of index
        #second number is index in poinots of this node
        minHN = [[0,0]]

        #loop happens edges number of times max, because is each time pop one neighbor from min
        #each time add to heap is logV
        #every time, take a node that is the closest neighbor to one in tree and then if it's not already in tree, add it's neighbors
        while len(tree) < N:
            #get min one that attaches to tree have so far (bc that's only way to get into this, is if you are a neighbor of a node added to tree)
            #node is nodeIndex in points list
            costToAttach, nodeIndex = heapq.heappop(minHN)
            #if node is in tree already, then can't add so don't do anything in this iteration
            if nodeIndex not in tree:
                #nc = neighbor cost
                #nni = neighbor node index
                tree.add(nodeIndex)
                res += costToAttach
                for nc, nni in adj[nodeIndex]:
                    #bc otherwise you'd be creating a cycle by adding this neighbor
                    if nni not in tree:
                        heapq.heappush(minHN, [nc, nni])

        return res
