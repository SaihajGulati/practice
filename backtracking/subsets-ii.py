class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #T: O(2^n * n) bc making copy part in base case as well as while loop are worst case N and have to do 2^n calls bc if all distinct, 
        #then 2^n subsets and have to do a call to get each one. Reason why 2^n is because each element can either be included or not
        #so, each level of the tree has two times the number of calls as last level, and we have n levels, so biggest order is bottom at 2^n
        #Extra M: O(n) bc of subset, because list outputting is ofc required so is not extra
        #but total memory is O(2^n * n) because max subset size is n and 2^n subsets
        
        res = [] # same as passing it each time bc is reference either way
        subset = [] #same as passing it each time bc either way is reference
        nums.sort() #key to whole shebang so that while loop below can skip all duplicates

        def dfs(i: int):
            #means have recursed off end
            #because even if is one length long combo, will eventually get to end because can either have the element in the subset or not, so if keep spamming check i of first not same in subset, then get here etc
            #for loop below makes it so that [] is the last one in res bc is going past end of for loop every time and calling on i until i == len
            if i == len(nums):
                res.append(subset[:])
                return
            
            #find all subsets that include this i
            subset.append(nums[i])
            dfs(i+1)
            #remove the one added so can try others
            subset.pop()

            #now find all ones that don't include this i or any of same number
            #first check is so that can access the index in the next check
            #need to use while loop to skip all others that are the same
            #because above version where automatically includes will include all ones that have that one and then next same etc etc or ones with none of same ones but including that one etc etc
            while (i + 1 < len(nums) and nums[i+1] == nums[i]):
                i += 1
            
            #will stop when first i + 1 is not i
            #so have to call with i+1 not i as i is still equal to one before it while i+1 is the different one
            #so now try without any of same ones included
            dfs(i+1)
            
        dfs(0)
        return res
        
