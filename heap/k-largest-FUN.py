class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #rewrite without using more memory
        #tho copying will probably use e
        #to use less memory, instead list comprehension, use for loop with number indexes to manually set
        #is same time complexity so all good
      
        #averagish case is O(n) with O(1) extra memory since setting to neg in place, but if k is close to n then approaches nlogn time complexity
        
        for i in range(0, len(nums)):
            nums[i] = - nums[i]

        heapq.heapify(nums)
        res = 0

        for i in range(k):
            res = heapq.heappop(nums)

        #last res is the one we want since does k times
        return -res
