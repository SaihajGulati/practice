class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # T: O(n)
        # M: O(1) since calculating difference in loop for each, not storing anything in list

        #if don't have enough gas to cover the costs (needs to cover all since need to go through all but can do so through any order)
        if sum(gas) < sum(cost):
            return -1

        
        #if get here, guaranteed solution

        #no greedy, first one we want that until the end of the array is all good is answer
        #bc:
        #all that end up with a total less than 0 before first that worked to end of array, failed
        #each value adds value (gas in the gas tank)
        #this gas reserve can help get us ready for the negative differences, especially the ones with the indexes we gave up on before this new start bc they made other tries fail
        #so, first one that makes it to end of array successfully, adds the most value and never failed as far as we can see
        #since we checked above that there is a solution, and we are guaranteed only one, the one that adds the most value (the one that starts first and makes it to the end) must be the answer
        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                #jump moves all the way up to past i NOT just one up
                #because one up will no matter what make you have less gas in the gas tank to cover the same amount of negative differences since:
                # if first index was negative, immediately tried next one
                # SO start must have been positive if made it far at all
                #and the i that made this fail must be negative to have lowered the total to a failable level
                # AND if that is the case, removing only the start and moving one up, will mean we have to cover the same amount of negatives coming after, the amount of negative differences that made the previous start with more gas overall fail
                #so would keep failing until start incremented up to the firist positive after all the negatives in this attempt came, which the earliest it could be is at i + 1
                
                start = i + 1
                total = 0
        #if get here, reached end of array with the start so that is answer
        return start


        
        
        #if got here, never found a way that works
        return -1
