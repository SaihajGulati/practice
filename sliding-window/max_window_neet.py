class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index
        #ok to have this slightly unnecesary l that requires a check, because already need a check for output array appending
        l = r = 0
        
      # T:O(n) M:O(n)
        while r < len(nums):
            # pop smaller values from q
            #have to do q check first
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            #SMART PART: putting in index instead of value, since don't have to sort by value or anything
            #if really wanted could also be tuple but no need
            q.append(r)

            # remove left val from window
            #since appended before this, don't have to do q check here --> SMART  
            if l > q[0]:
                q.popleft()
      
            #making sure right index is big enough that at least a k window has been made (bc at start will have max without valid window)
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
