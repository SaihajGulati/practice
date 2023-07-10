class Solution:
    def rob(self, nums: List[int]) -> int:
      #top-down
        one = 0
        two = 0

      # T: O(n) M O(1)
        for i in nums:
            temp = max(i + two, one)
            two = one
            one = temp

      #here since maxing each time handles start choosing, just return last one
        return one
