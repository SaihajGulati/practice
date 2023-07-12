class Solution:
    def jump(self, nums: List[int]) -> int:
        #top-down dp, worst bc of memory issue here bc rewriting front
        # T: O(n^2) bc for each i (no total), you go jumps number of times which can be at worst all of n
        # Extra M: O(N)
        numJumps = [1001] * len(nums)
        numJumps[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, min((i + nums[i] + 1), len(nums))):
                numJumps[j] = min(1 + numJumps[i], numJumps[j])
                print(numJumps[j])
        print(numJumps)  
        return numJumps[-1]
                hes for this window
            farthest = 0 #technically could/should be l, but either way bc first max below will override
            #window of new values included by last time went farthest
            for i in range(l, r + 1):
                #compute farthest we can end up with this batch of jumps
                farthest = max(farthest, i + nums[i])
            l = r + 1 #bc this is where new values start
            r = farthest
            numJumps += 1 #bc this window check means one jump is taken 
        
        return numJumps


                
