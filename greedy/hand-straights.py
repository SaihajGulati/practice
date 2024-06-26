#T: O(nlogn), no matter if use queue (n logn operations) or list (nlogn to sort)
#M: O(n)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        distinctValues = []
        minIndex = 0
        count = {}

        #create hashmap of counts and the distinct values list for mins
        #could make the mins list later easier using distinctValues = list(count.keys())
        for c in hand:
            #get default value of 0 or count and add one
            count[c] = count.get(c, 0) + 1
            if count[c] == 1: #because means this is the first one seen of it
                distinctValues.append(c)
        
        distinctValues.sort() #queue would be heapify here instead

        while minIndex < len(distinctValues):
            currMin = distinctValues[minIndex]
            if count[currMin] != 0: #otherwise skip and try with next value
                for i in range(currMin, currMin + groupSize):
                    #meaning none of this number left to work with
                    if i not in count or count[i] == 0:
                        return False
                    count[i] -= 1
            else:
                minIndex += 1
        
        #if make it all the way here, made it
        return True
