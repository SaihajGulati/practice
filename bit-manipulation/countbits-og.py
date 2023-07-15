class Solution:
    def countBits(self, n: int) -> List[int]:
        #T: O(n) M: O(1) bc no extra mem other than what returning
        #base case since need to access 0th first thing just set
        #and works bc n is lowest 0 which means array of size 1 where this is returned
        res = [0]

        place = 0

        for i in range(1, n + 1):
            #if same biggest place (bc not equal to the bigger place yet)
            if i < 2 ** (place + 1):
                #then you know is a one (for the place) + the difference between the place power and how much we've increased from iit
                #essentially using memoization
                res.append(1 + res[i - 2 ** place])
            else: #when is equal to the bigger place, it's a 1 time and update place
                res.append(1)
                place += 1

        return res
