class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        #alternate approach graph =  {i : [] for i in range(1, n + 1)}
        
        #want to sort by time in tuple, so make a tuple that way
        #it's ok to lose the info about what node it's from
        for u, v, t in times: 
            #(cost, end node) because want to sort by cost
            #source of the edge is the key of the hashmap
            graph[u].append((t, v))

        visited = {k}
        #counter of time it will take
        maxTime = 0
        minHeap = graph[k] #starts with edges from k
        heapq.heapify(minHeap) #sort by time

        if n == 1: #eliminates needing to check at start of for loop and after exit it
            return 0

        while minHeap: 
            #this is an edge being popped, so topV is the new node we've reached
            topT, topV = heapq.heappop(minHeap)
            #only process if not visited
            #don't need check here for if topV not in visited (since do below and bc of if n==1 statement above)
            #bc the case where a bunch to itself already covered above, and below gets rest
            visited.add(topV)
            if topT > maxTime: 
                maxTime = topT
            if len(visited) == n: 
                return maxTime
            #add neighbors
            for t, v in graph[topV]:
                if v not in visited:
                    heapq.heappush(minHeap, (topT + t, v))
        return -1
        #technically could just do check here because rest would create cycles after find shortest paths
        #but your method exits as soon as found so saves computation



        
