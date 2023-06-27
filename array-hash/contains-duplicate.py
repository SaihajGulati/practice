class Solution(object):
    """
    - story (of problem in terms of what should do): check if has duplicccate
    - input: integer array
    - output: boolean
    - Requirements: return true if there is duplicate, false if all unique
    - Constraints that could help:
    - Algo (thinking of): use hashSet to track what you have seen 
- */
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsSeen = set()
        for i in nums:
            if i in numsSeen:
                return True
            numsSeen.add(i)
        return False
