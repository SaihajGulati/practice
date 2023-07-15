class Solution:
    def countBits(self, n: int) -> List[int]:
        #T: O(n) M: O(1) bc no extra than what returning

        #this is faster than append bc of occasional copying over with append
        #even if has to put 0s in
        #also more like other languages where in this code where know size, wayyyyy better to initialize normal array with given length
        dp = [0] * (n + 1)

        #will be number that is the power of the place
        #ex 32 if place is 5
        #slightly faster than my og solution bc calculating power each time in loop takes longer
        #than straight multiplication
        placeOffset = 1

        #smarter to just store
        for i in range(1, n + 1):
            #so if this number has reached the next place, then change place and put 1 bc it is the next place/power
            if placeOffset * 2 == i:
                dp[i] = 1
                placeOffset = i
            #will be 
            else:
                dp[i] = 1 + dp[i - placeOffset]
            
            """ simpler code way that's slower bc requires you to so subtraction of potentially large numbers even when you konw will end up 0
            #so if this number has reached the next place, then change placeOffset bc this is the next power of 2
            if placeOffset * 2 == i:
                placeOffset = i
            #will be 
            dp[i] = 1 + dp[i - placeOffset]
            """
        return dp
