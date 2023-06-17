class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                #append adds reference by default, and here we need reference to copy then, because can't just have pointer added to res
                #res.append(subset[:])
                res.append(list(subset))
                return
            # decision to include nums[i] --> option
            subset.append(nums[i])
            #recursive call for next
            dfs(i + 1)
            # decision NOT to include nums[i] --> undo AND other option
            subset.pop()
            #recursive call for next with new/only other option
            dfs(i + 1)

        dfs(0)
        return res
