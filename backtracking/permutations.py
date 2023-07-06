class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        #T: O(N*N!) bc similar to most, bottom part/leaves dominates number of calls
        #and the leaves are permutations which by math there are n! of
        #takes n work each time max, because of both base case and for loop
        #M: O(N!) if talking about what we are returning, which is all permutations
        #Extra space is possibly on O(n) because recursion goes till n+1 layers max so recursive stack's max size is that
        #in other languages have to pass nums and res too in separate ofc
        def dfs(start):
            if (start == len(nums)):
                #: is cheatcode for copying bc makes a new list with references to items inside
                res.append(nums[:])
                return

            #tries swapping every single one with start one and returns ensuing lists
            for i in range(start, len(nums)):
                #swaps them, finds all permutations with start this i
                #other option of either popping from star and adding after takes O(n) for pop OR if do way to send array without it, 
                #then requires making copy of each half so is O(n) too while this way is O(1) time AND memory on the swap
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start+1)
                #unswaps them so can try next swap
                nums[start], nums[i] = nums[i], nums[start]
        dfs(0)        
        return res
