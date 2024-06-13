class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        curr = []
        #in other languages would have to pass curr to each function and overall result too, but in python can have both outside (better to have lists that are passed by reference outside but not variables)
        def helper(i, total):
            #this could be unlimited number of same checks OR any other combo
            if (total == target):
                result.append(curr[:])
            #otherwise only run if number has ways to go or index does (bc other two are base cases where isn't valid combo so don't add)
            elif (total < target and i < len(candidates)):
                curr.append(candidates[i])
                #check first option, which is having this (next one is also this though because unlimited number of times until backtrack)
                #works because tries all that have this value at this spot, so literally every option is checked
                helper(i, total + candidates[i])
                
                #undo
                curr.pop()

                #check other option which is not included next
                helper(i+1, total)
                
        helper(0, 0)
        return result
