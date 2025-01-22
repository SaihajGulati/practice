class Solution:
    #T: O(hi-lo * max power of x --> 2^31 + nlogn for sorting)
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        stepList = []
        for i in range(lo, hi + 1):
            x = i
            steps = 0
            while x != 1:
                steps += 1
                if x % 2 == 0:
                    x /= 2
                else:
                    x = 3 * x + 1
            stepList.append((i, steps))

        #1,0 because sorting by number of steps/power first, and then use actual value as tiebreaker if needed
        sortedList = sorted(stepList, key = operator.itemgetter(1, 0))

        return sortedList[k-1][0]
            

        
