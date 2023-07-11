class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # MEMOIZATION
        # Time: O(n*m)
        # Memory: O(n*m)
        #so have to use index to represent coins
        dp = [[None] * amount for i in range(len(coins))]

        #i is index, n is amount left
        def dfs(i, n):
            if n == amount:
                return 1
            if n > amount:
                return 0

            if i == len(coins):
                return 0

            if dp[i][n]:
                return dp[i][n]

            #have two options, include this one or not
            #can do this way because order of coin denominations does not matter so thsi will get all options and only need tocheck once which is why i == len check is above
            dp[i][n] = dfs(i, n + coins[i]) + dfs(i+1, n)

            return dp[i][n]

        return dfs(0, 0)
