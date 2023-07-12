class Solution:
    def jump(self, nums: List[int]) -> int:
        #bottom-up dp --> in between solution, og solution i got, fun but not optimal optimal
        #T: O(n^2) bc have to do n for outer for loop and inner does max n each time if jumps was big enough
        #Extra M: O(1) but requires writing over given list (ask in interview if can)
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= len(nums) - 1:
                nums[i] = 1
            else:
                #need max number right now so min automatically replaces each time even if size of array is bigger than max value (1001)
                #which could lead to number of jumps bigger than 1001 and don't want 1001 becoming min
                #good to be safe and just use inf for this situation
                minJumps = float("inf")
                #min is important bc can't go off end
                for j in range(i + 1, min((i + nums[i] + 1), len(nums) - 1)):
                    #have to add 1 because not using 0 here
                    minJumps = min(minJumps, nums[j])
                nums[i] = 1 + minJumps
                print(nums[i])
            
            #print(nums[i]) 


        return nums[0] if len(nums) > 1 else 0
