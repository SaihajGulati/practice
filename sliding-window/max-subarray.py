class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for i in nums:
            currSum += i
            #make sure to check max before reset curr, because otherwise would falseley make 0 the maxSum if it was less than 0
            maxSum = max(currSum, maxSum)
            #this check is because if prefix part is negative, then is irrelevent and don't need/want it in subarray
            if currSum < 0:
                currSum = 0

        return maxSum
