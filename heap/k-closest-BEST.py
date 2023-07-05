class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #T: O(n) M: O(n)
        minHeap = []

        #O(n) operation
        for x, y in points:
            #avoid doing sqrt as is unnecessary because we don't need actual distance, 
            #just what is bigger/smaller which can be checked without sqrt being there as it won't change relative largeness
            #is really distance formula but since is from 0, the 0s are invisible and also not sqrting to save time
            #but dangerous game bc still have to square each to get correct differences so if ever a bit confused on whether can, just be safe
            dist = x**2 + y**2
            minHeap.append([dist, x, y])

        #heapify automatically sorts by first value in array
        #O(n) operation
        heapq.heapify(minHeap)

        res = []

        #O(k)
        for i in range(k):
            #this variable naming setup in python is cracked
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res
