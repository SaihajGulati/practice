class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #to store previous interval
        
        #sort by the 0/start value for each x in intervals
        intervals.sort(key = lambda x: x[0])
        
        prev = intervals[0]
        result = []

        for curr in intervals:
            #if previous's end is greater than or equal to current's start, 
            #then is overlapping as is guaranteed by sort that start is less than or equal to, 
            #and equal to case is handled by fact end of each intervals has to be equal to or bigger than its start
            if prev[1] >= curr[0]:
                curr[0] = min(prev[0], curr[0])
                curr[1] = max(prev[1], curr[1])
            else: #is not overlapping so add previous (NOT CURR YET BC NEED TO CHECK IF OVERLAPPING)
                result.append(prev)
            prev = curr
        
        #if last one satisfied first if statement then is not added, else last one is added so need to check
        #if last one in result is not the prev, then add prev
        if len(result) == 0 or result[len(result)-1] != prev:
            result.append(prev)

        return result
