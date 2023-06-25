class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        #T: O(n) M: O(n)
        #could do diff ways with split up looping to append at end and start, but ends up being more complex for same runtime bc deep copy requires looping over all anyways, just less code
        for i in range(len(intervals)):
            #if the end of the interval checking is less than new one's start, add to result because is cleanly before
            if (intervals[i][1] < newInterval[0]):
                result.append(intervals[i])
            #otherwise if the start of the interval is after the end of the new one (so cleanly after)
            elif (intervals[i][0] > newInterval[1]):
                result.append(newInterval)
                return result + intervals[i:]
            #if get here, is not cleanly before or cleanly after
            #can just do mins and maxes because already know is not clean
            #setting 0th and 1th is better than doing newInterval = [min(intervals[i][0], newInterval[0]), max(newInterval[1], intervals[i][1])]
            #doing that means make new list each time which means it needs to allocate memory each time rather than constant time access
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        #this is needed to handle cases where needs to be inserted at end
        result.append(newInterval)
        return result
