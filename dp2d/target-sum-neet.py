class Solution:
  #his solution is like mine but instead of sumLeft he just does sum
  # T: O(nt) bc range of index is n and range of totals for each index is 0 + t and 0 - t where t is total of entire array summed up
  # M: O(nt)
  #so range is 2t and that's O(t) so O(n) * O(t)
  #only worry about range of variables for runtime bc for cases where see again, don't do amount of work we do for rest,
  #so asymptotic means those ones don't really have an impact
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)
