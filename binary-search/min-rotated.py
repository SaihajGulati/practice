class Solution:
    def findMin(self, nums: List[int]) -> int: 
        m = 0
        l = 0
        r = len(nums) - 1

        #T: O(logn) #M: O(1)
        while l <= r:
            m = (l+r)//2
            #this check is key
            #check if equal, which means is lower than stuff on both sides
            #modulus is cheat code and so is -1 on left
            if nums[m] < nums[m-1] and nums[m] < nums[(m+1)%len(nums)]:
                return nums[m]
            #so if not less than both sides, then is it bigger than end?
            #if is bigger than end, then pivot/reset happens on right because otherwise impossible in sorted list to get smaller on right
            elif nums[m] > nums[-1]:
                l = m + 1
            #else you gotta look behind
            else:
                r = m - 1
        return nums[m]
