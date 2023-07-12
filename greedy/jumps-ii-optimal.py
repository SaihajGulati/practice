class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = numJumps = 0
        # T: O(n) bc only going through list once in total as only go through new window each since that's a jump
        # M: O(1)
        while r < len(nums) - 1:
            #new farthest for this window
            farthest = 0 #technically could/should be l, but either way bc first max below will override
            #window of new values included by last time went farthest
            for i in range(l, r + 1):
                #compute farthest we can end up with this batch of jumps
                farthest = max(farthest, i + nums[i])
            l = r + 1 #bc this is where new values start
            r = farthest
            numJumps += 1 #bc this window check means one jump is taken 
        
        return numJumps


                
