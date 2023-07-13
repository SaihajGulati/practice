class Solution:
    #T: O(nlogn) bc of sort don't forget that
    # M: O(1)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        prevEnd = float("-inf") #so anything is bigger than this so first value immediately does not have a

        intervals.sort() #will sort by first value and then second one as tiebreaker

        res = 0

        for start, end in intervals:
            #if this interval's start is less than the previous one's end (then they are overlapping since start must be same or greater bc of sort)
            if start < prevEnd:
                res += 1
                #save one that end first bc means less chance of overlapping with next
                prevEnd = min(prevEnd, end)
            #else they are not overlapping so continue with keeping this but update prev
            else:
                #update end bc it's like keeping this
                prevEnd = end

                 
        return res
