class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        #getting rid of added boolean means in that if statement can return immediately which fills in rest of array faster
        #than if checked all if statements for subsequent times when know have added
        #T: O(n) M: O(n)
        #could do diff ways with split up looping to append at end and start, but ends up being more complex for same runtime bc deep copy requires looping over all anyways, just less code
        for i in range(len(intervals)):
            #if the end of the interval i is less than new one's start, add to result because i interval is cleanly before
            if (intervals[i][1] < newInterval[0]):
                result.append(intervals[i])
            #if that's the case and the start of i interval is after the end of the new interval's end (so i interval is cleanly after the new one
            elif (intervals[i][0] > newInterval[1]):
                result.append(newInterval)
                return result + intervals[i:]
            #if get here, i interval is not cleanly before or cleanly after
            #can just do mins and maxes because already know is not clean so we are going to combine
            #setting 0th and 1th is better than doing newInterval = [min(intervals[i][0], newInterval[0]), max(newInterval[1], intervals[i][1])]
            #doing that means make new list each time which means it needs to allocate memory each time rather than constant time access
            else: #make new interval equal to bigger one and then checks of next time can help use find out 
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        #this is needed to handle cases where needs to be inserted at end
        #don't have to check if added, because once is added, is immediately returned with rest of list copied over
        #so only gets here if not yet added
        result.append(newInterval)
        return result
