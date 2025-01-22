class Solution:
    #T: O(logn)
    #M: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        start = -1
        #finding starting index
        while (l <= r):
            m = (l + r) // 2
            if (nums[m] == target and (m == 0 or nums[m-1] != target)):
                start = m
                break
            elif nums[m] == target or nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        if start == -1:
            return [-1, -1]
        elif start == len(nums) - 1 or nums[start + 1] != target:
            return [start, start]

        l = 0
        r = len(nums) - 1
        end = -1
        #finding ending index
        while (l <= r):
            m = (l + r) // 2
            print(m)
            if (nums[m] == target and (m == len(nums)-1 or nums[m+1] != target)):
                end = m
                break
            elif nums[m] == target or nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return [start, end]
                
        



        
