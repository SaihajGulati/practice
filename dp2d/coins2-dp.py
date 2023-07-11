class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
       # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n*m)

        #array that is coins in each row + 1 times amount + 1 rows
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]

        #first row (so when have 0 left) is all 1s bc is base case as there is one way to get there clearly
        dp[0] = [1] * (len(coins) + 1)
        #above makes it so that extra column is already 0 at end

        #first solution neet shows drawn weirdly bc he's setting up for next one but this is how written if you tilt his drawin
        #traverse through amounts (go through column downwards)
        for a in range(1, amount + 1):
            #go backwards through this row of coin denominations
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                #if can get to number before run out of amount, is a possible way so add the ways to get from there to 0 to what we have right now
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]
