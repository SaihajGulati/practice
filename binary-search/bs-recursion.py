class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binarySearch(l, r):
            if l > r:
                return -1
            m = int((l+r)/2)
            if nums[m] > target: 
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
            return binarySearch(l, r)
        
        return binarySearch(0, len(nums)-1)
