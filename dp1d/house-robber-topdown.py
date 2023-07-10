class Solution:
    def rob(self, nums: List[int]) -> int:
      #top-down
        rob1 = 0
        rob2 = 0

      # T: O(n) M O(1)
        for i in nums:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp

      #here since maxing each time handles start choosing, just return last one
        return rob2
