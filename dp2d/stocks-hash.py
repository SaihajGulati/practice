def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        #T: O(n) bc 2n in hashmap, so will run max that many times too since other times will just use that solution
        #M: O(n) bc of hashmap
        #idk why tf neet used a hashmap here instead of 2d-list
        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
