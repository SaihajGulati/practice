class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #T: O(n) #M: O(1)
        result = 0

        #works bc:
        #with xor, n ⊕ 0 always is n, because if 1, then evaluates to 1 and if is 0, evaluates to 0.
        #So, if xor all of them starting with 0, first will become itself, 
        #and then all duplicates will cancel out eventually to 0 bc is xor, and only one left will be different one. 
        #^ (xor) is a cheatcode for this type of find different problems
        #
        for n in nums:
            result = n ^ result
        return result
