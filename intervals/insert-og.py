class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        added = False

        #could do diff ways with split up looping to append at end and start, but ends up being more complex for same runtime bc deep copy requires looping over all anyways, just less code
        for i in range(len(intervals)):
            #if the end of the interval checking is less than new one's start, add to result because is cleanly before
            if (intervals[i][1] < newInterval[0]):
                result.append(intervals[i])
            #otherwise if the start of the interval is after the end of the new one (so cleanly after)
            elif (intervals[i][0] > newInterval[1]):
                if not added:
                     #need to put in if is first that clears
                    result.append(newInterval)
                    added = True
                #need to do regardless of whether add in new or not
                result.append(intervals[i])
            #if get here, is not cleanly before or cleanly after
            #need this setup so can check both ifs, not just one
            #as both can be true
            else:
                #if not cleanly before, need to update new's startpoint, and don't need to add anything as this interval is merged with new
                if intervals[i][1] >= newInterval[0]:
                    newInterval[0] = min(intervals[i][0], newInterval[0])
                #if not cleanly after, swallow each other
                if intervals[i][0] <= newInterval[1]:
                    newInterval[1] = max(newInterval[1], intervals[i][1])
        if not added:
            result.append(newInterval)
        return result
