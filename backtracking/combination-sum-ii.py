#T: O(2^n) because going through all 
#M: O(2^n) because that many in stack to unpack
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() #approach is sort and then if don't include, skip all of same number
        result = []
        curr = []

        def backtrack(pos, targetLeft):
            if targetLeft == 0:
                #needs to be a copy because is being changed live
                result.append(curr.copy())
                return
            elif targetLeft < 0: 
                return
            #case of pos out of bounds don't have to handle here 
            #because will not enter for loop below if out of bounds

            prev = -1
            #can't do len-1, because then will never enter loop for last one
            for i in range(pos, len(candidates)):
                #getting here means did not include last time
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, targetLeft - candidates[i])
                curr.pop() #removes from end
                #don't call again, because is in for loop implicitly
                #same targetLeft but one more i
                prev = candidates[i]
        
        backtrack(0, target)   
        return result



        
