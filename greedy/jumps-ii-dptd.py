class Solution:
    def jump(self, nums: List[int]) -> int:
        #top-down (moving foward) dp, WORST bc of memory issue here bc rewriting front
        # T: O(n^2) bc for each i (no total), you go jumps number of times which can be at worst all of n
        # Extra M: O(N) bc extra array needed
        #on leetcode, didn't even pass bc of time/memory limit, proof of top-down not always better

       #need max number right now so min automatically replaces each time even if size of array is bigger than max value (1001)
       #which could lead to number of jumps bigger than 1001 and don't want 1001 becoming min
       #good to be safe and just use inf for this situation
        numJumps = [float("inf")] * len(nums)
        numJumps[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, min((i + nums[i] + 1), len(nums))):
                numJumps[j] = min(1 + numJumps[i], numJumps[j])
                print(numJumps[j])
        return numJumps[-1]  


                
