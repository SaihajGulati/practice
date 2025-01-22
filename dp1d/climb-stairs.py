class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Final Solution -- T: O(n) M: O(1)
        
        one, two = 1, 1

        #only n - 1 times
        #each time, getting number of ways to get to that stair, temp = one + two because from one down or two down
        #range(n-1) because this is from 2 to n (inclusive) --> (2, n+1)
        for i in range(n-1):
            temp = one + two
            #move two back to where one is right now
            two = one
            #move one back to where curr is right now for next
            one = temp
        
        #with ex, runs 4 times, where last one is last temp, which is answer
        return one
