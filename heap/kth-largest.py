class KthLargest:

    def __init__(self, k, nums):
        # minHeap w/ K largest integers
        #heap is by default minheap, and by keeping on popping, we keep on taking away smallest one
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        #this needed because if less than k, then add no matter what and handles null case which need to check since accessing next
        if (len(self.minHeap) < self.k):
            heapq.heappush(self.minHeap, val)
        #this check saves HELLA runtime because push is logn operation (here logk) while pop is an additional O(logk), but can check first in O(1) and never have to do those
        elif (val > self.minHeap[0]):
            heapq.heappush(self.minHeap, val) 
            #since checked < k, and added then and when length is k we don't enter this bc of elif, we don't have to check anything here
            #otherwise would have to check before popping that length is bigger than k           
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
