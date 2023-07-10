class Solution:
    def rob(self, nums: List[int]) -> int:
        #end is exclusive
        def helper(start, end):
            one = 0
            two = 0
            for i in range(start, end):
                temp = max(nums[i] + two, one)
                two = one
                one = temp
            return one

         #whole idea is how in before version you did same thing twice and only checked end one if didn't start with that one
        #so run from start but not incl end, and then incl start but not end
        #ALSO compare with num[0] to handle case of list of size 1
        return max(helper(1, len(nums)), helper(0, len(nums) - 1), nums[0])
