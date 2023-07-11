class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
       # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount WHICH IS CRACKED

        #1d of amounts left, + 1 so that can have 0th index as base for one way if get there bc is a success(1)
        dp = [0] * (amount + 1)
        dp[0] = 1
      
        #work backwards through list of coins, bc do for each coin denomination working through amounts allows for only needing two arrays
        for i in range(len(coins) - 1, -1, -1):
            #next array is this  since moving through coins and so only need 1d at a time really
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            #go forward through amounts (again his drawing is wack)
            for a in range(1, amount + 1):
                #this row is the row of this amount we are working on (what we will access left of (in his drawing right))
                #BUT we set to old row value of this coin (one below us)
                nextDP[a] = dp[a]
                #means change of being possibly combo
                if a - coins[i] >= 0:
                    #works because need to access
                    #add one below us's value to one on left (right in his drawing) IN THIS ROW so what previously did in this inner loop
                    nextDP[a] += nextDP[a - coins[i]]
            #update so ready for next coin move up
            dp = nextDP
        return dp[amount]
