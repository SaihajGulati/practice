class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #key = (i, buy/sell)
        #val = max profit
        dp = {}

        #T: O(n) bc 2n in array, so will run max that many times too since other times will just use that solution
        #M: O(n) bc of array
        #leetcode says this is slightly faster and less memory, maybe just bc array indexing simpler than hashing tuple
        #this code relies on fact that boolean uses 0 and 1 values, could ofc manually subtract 1 or add to change too if didn't for some reason

        #row for each price with two spots in it for buying/selling
        dp = [[None] * 2 for i in range(len(prices))]

        #0 is selliing and 1 is buying
        def dfs(i, buying):
           #can't get more profit if recursed off
           #>= is good always but > is bc of i + 2 recursion part
            if i >= len(prices):
               return 0
            
            #USE CACHE
            #if it's not none, return it
            if dp[i][buying]:
                return dp[i][buying]

            #if choose not to do anything, and continue with same option of buying/selling with next i to calculate
            noAction = dfs(i + 1, buying)

            if buying:
                #not buying bc gets switched (here from buying to selling since now bought)
                buy = dfs(i + 1, not buying) - prices[i]
                dp[i][buying] = max(buy, noAction)
            else:
                #not buying bc is opposite so from selling to buying now since sold
                #i + 2 because cooldown means can't do anything at i+1
                sell = dfs(i + 2, not buying) + prices[i]
                dp[i][buying] = max(sell, noAction)
        #easiest with tis return statement so can do dfs and compare results as do above
            return dp[i][buying]

        return dfs(0, True)
