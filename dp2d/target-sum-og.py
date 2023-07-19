class Solution:

#neet solution is super similar but instead of sumLeft, he does sum
#that means if statement checks if sum == target, not 0, and this method is initially called with backtrack(0, 0) instead of 0, target

#T: O(nt) where go through each index, and for reach the sumLeft is in range 0 to target plus total of array values summed up which is 2 times it (2t) so O(t)
  
#M: O(i
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #use hashmap bc with 2d array in other languages cannot have null as starting value so no way to set starting value to somethig will never reach
        def dfs(index, sumLeft):
            #only way bc has to be that at end have reached target
            if index == len(nums):
                if sumLeft == 0:
                    return 1
                else:
                    return 0
            #if find something that already seen, just return what it was for that
            elif (index, sumLeft) in dp:
                return dp[(index, sumLeft)]
            


            #if get here, need to store and return need to run for both plus and negative
            dp[(index, sumLeft)] = dfs(index + 1, sumLeft - nums[index]) + dfs(index + 1, sumLeft + nums[index])
            
            #return it so that can return up stack to do addition above
            return dp[(index, sumLeft)]

        #start off with index 0 and target amount left
        return dfs(0, target)
