class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        ##constant extra space, so cannot have hash set of things that help you get to sum, and then means only make answer array at end
        #good to have terminating as soon as pass loop just in general 
        while left < right:
            #good to access these just once because it saves some time and memory
            sum = numbers[left] + numbers[right]
            if (sum == target):
                ##remember to return indices here not values, and plus 1 because 1 index
                return [left + 1, right + 1]
            elif (sum < target):
                left += 1
            else: #otherwise is bigger than target
                right -= 1
