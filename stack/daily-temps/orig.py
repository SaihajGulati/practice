#T: O(n)
#M: O(n) or O(1) extra if say is required to make result array separate
#But is worse than Neet's because use two separate stacks instead of one of tuples
#and do while loop at end for no reason even though result is filled with 0s already
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        valStack = []
        indStack = []
        #could do in place too, but bad practice typically
        result = [0] * len(temperatures)

        for index, num in enumerate(temperatures):
            #end if top of stack
            #if greater than, time to update
            while valStack and num > valStack[-1]: 
                valStack.pop()
                i = indStack.pop()
                #number of days until hit higher one
                result[i] = index - i

            #do at end otehrwise if statement will never be true
            valStack.append(num)
            indStack.append(index)
            
        
        #reach end of list here, so no days higher after
        while valStack:
            valStack.pop()
            i = indStack.pop()
            result[i] = 0
        

        return result



        
        
