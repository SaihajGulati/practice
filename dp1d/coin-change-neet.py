class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #max number of coins is amount, because would require all 1s
        #so if start with amount + 1 as default, can use this as max
        dp = [amount + 1] * (amount + 1) #start with this as base value
        #this needs  to be zero however despite above for dp to work
        dp[0] = 0


        #imagine dp is from 0 left to amount left
        for i in range(1, amount + 1):
            #have to try every coin
            for c in coins:
                #if in bounds to try with coin c and there is a path
                #works because if c > i, stays amount + 1
                #OR if end up with i >= c but no way to get to amount with i - c, will check min of amount + 1 and amount + 1 + 1 so stays amount + 1
                #if 
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i - c])

            
        #do this check at the end bc of what explained above
        return dp[amount] if dp[amount] != amount + 1 else -1
