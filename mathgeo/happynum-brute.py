class Solution:
    def isHappy(self, n: int) -> bool:
        #T: O(n) but probably worse than the optimal cause n is kinda confusing here
        #M: O(n) which is real issue
        seen = set()

        while n != 1:
            #bc means is a cycle
            if n in seen:
                return False
            
            num = n
            newN = 0
            while num > 0:
                digit = num % 10
                newN += (digit * digit)
                #remember in python floor division
                num //= 10

            #add n to ones we've seen
            seen.add(n)
            n = newN
            print(n)


        #if get here, n = 1
        return True
