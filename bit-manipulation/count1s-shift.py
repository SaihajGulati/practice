class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #T: 0(32) bc length is set
        count = 0
        while n:
            #more intuitive, is same as dividing by 2 each time which I was thinking
            #returns 1 if last one is 1 (odd), otherwise will return 0 and thus add 0 to count
            count += n % 2
            #n = n >> 1
            n >>= 1
        return count
