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
            ##python divides with decimials by default BUT converts it to int where needed
            ##so technically need this if want int but don't need because when use m to access array, converted to int
            m = int((l+r)/2)
            if nums[m] > target: 
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
            return binarySearch(l, r)
        
        return binarySearch(0, len(nums)-1)
