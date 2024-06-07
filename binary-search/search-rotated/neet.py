#T: O(logn)
#M: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            #if left is properly sorted
            if nums[l] <= nums[mid]:
                #if is in any of the two cases where could be on the right (target bigger than all on left, or looping around from left) 
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #right is properly sorted      
            else:
                #if is in any of the two cases where could be on the left (target smaller than all on right or looping around from right) 
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
