class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #T: O(n)
        #T: O(1)
        result = [0] * len(nums)
        result[0] = 1 #will be changing stuff here, not changing nums which is a good practice generally
        #result will have running left products (prefix)
        #nums will have correct number

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        R = 1 #running right count that just directly multiply so avoid third for loop, and this way don't change nums array which is good practice
        for i in reversed(range(len(nums))):
            result[i] *= R
            R *= nums[i]
        
        return result

        
