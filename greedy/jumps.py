#python3 activated for better memory for things under the hood
class Solution:
    def canJump(self, nums: List[int]) -> bool:
       #original goal is end
        goal = len(nums)-1

        #start at second to last index because only need to get to last index
        #reversed means biggest is still exclusive and bottom isn't
        for i in reversed(range(len(nums)-1)):
            #if the max number of jumps from her gets you to last or past, new goal
            if i + nums[i] >= goal:
                goal = i

        #if there is a solution, at the end can reach goal and so goal will be at start
        return goal == 0 
