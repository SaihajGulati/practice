class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #to store previous interval
        
        #sort by the 0/start value for each x in intervals
        intervals.sort(key = lambda pair: pair[0])

        result = [intervals[0]]

        #so useful to be able to do this with for loop
        for start, end in intervals:
            prevEnd = result[-1][1]
            #if previous's end is greater than or equal to current's start, 
            #then is overlapping as is guaranteed by sort that start is less than or equal to,
            #and equal to case is handled by fact end of each intervals has to be equal to or bigger than its start
            if prevEnd >= start:
                result[-1][1] = max(prevEnd, end)
            else: #is not overlapping so add this one
                result.append([start, end])
        
        #just putting into array by default, and editing there if needed, 
        #eliminates if statements here which maybe makes slightly faster but definitelys simplifies code
        #good to just do as soon as can if access is same

        return result
