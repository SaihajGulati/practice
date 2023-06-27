class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        options = {}
        #enumerate is cracked when you need the index and value
        for i, num in enumerate(nums):
            diff = target - num
            #if what you need is in the dictinoary, you found it
            if diff in options:
                return [options[diff], i]
            else: #didn't find it yet, so add this value and it's index in
                options[num] = i
