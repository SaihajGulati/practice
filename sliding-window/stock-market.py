class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        maxProfit = 0

        while (right < len(prices)):
            #means found one even less, make left to that to check
            if (prices[right] < prices[left]):
                left = right
                right = left + 1
            #means right is bigger than left, so potential profit
            else:
                profit = prices[right] - prices[left]
                if (profit > maxProfit):
                    maxProfit = profit
                right += 1
        return maxProfit
