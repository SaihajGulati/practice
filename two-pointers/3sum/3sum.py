class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        #T: O(n^2)
        
        for i, val in enumerate(nums):
            #skip if is positive, as need to only check negatives bc can't have zero sum without a negative
            if val > 0:
                break

            #check if next one is same
            #checking prevoius vs next is better, becaue using the first to start ensures that sums that use same number if at different index are looked at, and yet that the same number is the one we analyze as the first number in triplet only once
            #also solves zero problem so don't have to check
            if i > 0 and val == nums[i-1]:
                continue #go to next because can't have duplicates
            
            l = i + 1
            r = len(nums)-1
            #sorting here allows for it
            while l < r:
                #check with r + 1 for same reason do l - 1 below
                """if r < len(nums) - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue"""
                # same reason to use l-1 to check, because first version of number will be looked at which here will not
                #will always be more than 0 because i + 1 and min i is 0
                #don't check l like r above bc l could be same as one before since could be val and part of triplet
                
                threeSum = nums[l] + nums[r] + val
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([nums[l], nums[r], val])
                    #have to change both as need to find all other solutions too
                    l += 1
                    r -= 1
                  #if didn't do this check, then would have to the quoted one above, but that's a lot slower somehow
                  #maybe bc by continuing, you are total checking for three conditions, while here you only check two
                  #also because you only check this condition in this one part of the if-else statement, you don't check it every time while loop runs
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
