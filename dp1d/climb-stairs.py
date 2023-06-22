class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1

        #only n - 1 times
        for i in range(n-1):
            temp = one + two
            #move two back to where one is right now
            two = one
            #move one back to where curr is right now for next
            one = temp
        
        #runs 4 times, where last one is last temp, which is answer
        return one
