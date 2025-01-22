class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Final Solution -- T: O(n) M: O(1)
        
        one, two = 1, 1

        #only n - 1 times
        #each time, getting number of ways to get to that stair
        for i in range(n-1):
            temp = one + two
            #move two back to where one is right now
            two = one
            #move one back to where curr is right now for next
            one = temp
        
        #with ex, runs 4 times, where last one is last temp, which is answer
        return one
