class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #order it so that you can eliminate the last onoe or use it
      
        #will store minimum speed, but starts with max, which is biggest pile
        #O(n) operation
        k = max(piles)

        if h == len(piles):
            #because if h is the length, then it is just automatically the largest so that can get each pile each time
            return k
        
        #otherwise need to do binary search bw 1 and max
        low = 1
        high = k

        #T: O(log(maxVal) * n) M: O(1)
        #binary search between 1 and maxValue, and n in time complexity comes from having to calculate hours for each pile, THO by using ceil with division each of those is O(1)
        while low <= high:
            #number we're checking right now
            #need truncacted toward 0, and floor does that for positive
            m = (low + high)//2
            hours = 0

            #go through each pile and calculate hours
            for p in piles:
                #fast way to calulcate hours
                hours += math.ceil(p/m)
                #this condition seems to slow the code down
                #probably because have to check it every time for a good solution which is most of the ones we will look at so barely saves time but adds hella bc need to check each time for p in pile
                """if hours > h:
                    break"""

            #if get here, either hours is more than h, or finished last pile with 0+ hours to spare
            if hours <= h:
                k = m
                high = m - 1
            #speed is too slow, so need to check higher only
            else:
                low = m + 1

        return k
