class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #T: O(n) M: O(n)

        #get top
        #check if bigger than one just added (right)
        #if isn't, one added is max, otherwise stays
        # and store as max of this sliding window in the answer
        #if left is top, pop
        #increase right and left

        right = 0
        q = deque()
      
        maxWindow = []

        while right < len(nums):
            #pop from left if one that is store max is now out of range
            if q and q[0] == right - k:
                q.popleft()

            #else if the new number is bigger than last, replace it
            #will keep doing due to while loop
            #need seperate q check here and stop condition
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            
            #add to end of list, as is either a new max
            #or a new value to be put in line to be max one day possibly
            q.append(right)

          #only add to output array if have a valid k window (bc at start are starting from index = 0 and haven't formed even one window yet but have a max)
            if (right >= k - 1):
                maxWindow.append(nums[q[0]])

            right += 1

        return maxWindow
