class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # T: O(nlogn)
        # M: O(n)
        stack = [] 
        res = [0] * len(temperatures)

        #don't need to save in tuple since can just save index and access
        for i, t in enumerate(temperatures): 
            # while the tempature is larger than the minimum's temp in the heap
            while stack and t > temperatures[stack[-1]]: 
                index = stack.pop() #set index to index of that temperature
                res[index] =  i - index #set the value
            
            #if get here, means not bigger than anything left (means stack will always be decreasing so smallest is at end)
            stack.append(i)

        return res


        
