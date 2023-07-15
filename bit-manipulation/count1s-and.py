class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #T: 0(# of 1s)
        count = 0
        while n:
            #each time, removes a one present in n
            #so, will only run number of times that n is present
            #n = n & (n-1)
            n &= (n-1)
            count += 1
        return count
