class Solution:
    #T: O(n)
    #M O(n) or O(1) if think result required
    #slightly better than original because just one stack of tuples, and no while loop at end (is handled by filling 0s in result at start)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #stack of pairs (temp value, index)

        #could do in place too, but bad practice typically
        result = [0] * len(temperatures)

        for index, num in enumerate(temperatures):
            #end if top of stack
            #if greater than, time to update
            #access index of stack top value
            while stack and num > stack[-1][0]: 
                stackVal, stackInd = stack.pop()
                #number of days until hit higher one
                result[stackInd] = index - stackInd

            #do at end otehrwise if statement will never be true
            stack.append((num, index))

        return result



        
        
