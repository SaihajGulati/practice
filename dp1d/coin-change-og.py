class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # T: O(amount * len(coins) M: O(amount)
        #if start with all zeros, then need manual tracking of min below
        #if start with amount + 1 as start of min value below, this is more intuitive than other version slightly and that's good, work with this then
        dp = [0] * (amount + 1) #start with this as base value


        #imagine dp is from 0 left to amount left
        for i in range(1, amount + 1):
            #coculd and should use amount + 1 as starting max value bc max number of coins is amount if all 1s
            minCoins = float("inf")
            #have to try every coin
            for c in coins:
                #if in bounds to try with coin c and there is a path
                if i >= c and dp[i - c] != -1:
                    #try to find minimum to get to this amount
                    minCoins = min(minCoins, 1 + dp[i - c])

            if minCoins == float("inf"):
                dp[i] = -1
            else:
                dp[i] = minCoins

        return dp[amount]








        


        

