class Solution:
    def isHappy(self, n: int) -> bool:
        #T: k * O(n) bc will find cycle after k number of constant cycles happen
        #M: O(1)
      
        #start fast one ahead here just to even more quicken it
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            #fast will go at double speed bc happens twice which is smart and so like with race in circle, if there is a cycle, will eventually end up at same spot again
            #like linked list cycle!
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        #will end either bc both are at 1 since is stuck there, or because there is a cycle found
        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        currSum = 0
        while n:
            #add digit to curSum
            currSum += (n % 10) ** 2
            #update but remember to do floor because by default is float division
            n = n // 10
        return currSum
