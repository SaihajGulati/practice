class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #T: O(knlogn) M: O(n)
      
        #pseudocode
        
        #set left and right
        #add first k to heap

        #get top
        #check if bigger than one just added (right)
        #if isn't, one added is max, otherwise stays
        # and store as max of this sliding window in the answer
        #if left is top, pop
        #increase right and left

        left = 0
        #bc of indexing, -1 it
        right = left + k - 1
        
        maxHeap =  []
        maxWindow = []

        #do k - 1 because of start of while loop
        for i in range(0, k - 1):
            #add the actual value and index
            #value first so is sorted by it
            #negative for value so is maxHeap
            maxHeap.append((-nums[i], i))

        #O(k)
        heapq.heapify(maxHeap)

        while right < len(nums):
            #add value just added to window
            #will remove invalid maxes/numbers later
            #O(nlogn)
            heapq.heappush(maxHeap, (-nums[right], right))

            #get top and make sure it's valid by checking index (second value of tuple)
            #will remove all maxes that no longer are in window
            #will never be bigger than right as not seen yet, so don't need to check
            #could happen as much as k times bc if find huge value at right after expanding, then have to remove all others eventually if gets out of window then
            #O(knlogn)
            while maxHeap[0][1] < left:
                heapq.heappop(maxHeap)
            
            #now the one on top is the max of this window
            #so add the value of it, which is first value of tuple to maxWindow
            maxWindow.append(-maxHeap[0][0])

            left += 1
            right += 1

        return maxWindow
