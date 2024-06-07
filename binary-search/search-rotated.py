class Solution:
  #T: O(logn)
  #M: O(1)
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            midVal = nums[m]
            leftVal = nums[l]
            rightVal = nums[r]
            if midVal == target: 
                return m
            if target > midVal: #typically on the right
                #check if pivot in between here and right
                #means all to left have to be smaller
                if midVal > rightVal: 
                    l = m + 1
                #no pivot, so check if past right looped around
                elif target > rightVal:
                    r = m - 1
                else: #no pivot on right and not past it
                    l = m + 1
            else: #target is less than midVal
                if target < leftVal:
                    l = m + 1
                else:
                    r = m - 1
        return -1
                



        
