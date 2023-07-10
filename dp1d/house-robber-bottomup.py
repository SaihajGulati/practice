class Solution:
    def rob(self, nums: List[int]) -> int:
      #bottom-up version
      #T: O(n) M O(1)
        two = 0
        one = 0

        #reverse keeps range's parameters, so this starts at len-1 and has 0 inclusive
        for i in reversed(nums):
            temp = max(i + two, one)
            two = one
            one = temp

        #have to max them since this way gives two choices for where to start that is never handled
        return max(one, two)
