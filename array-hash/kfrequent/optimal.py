# O(n) time complexity, O(n) memory complexity with a hashmap of size n, another list of size n, and a result list of size k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            #increment by 1, with 0 as the default value
            count[i] = count.get(i, 0) + 1

        #each index of this is one less than the frequency it repesents
        #for instance, index 0 is a list of all element values that have a frequency of 1 in the original list
        #initialized to empty list because all are lists
        #is list of list of elements with that index + 1 frequency
        #could also just do len + 1 and then avoid indexing shenanigans below
        freqLists = [[] for i in range(len(nums))]

        #fills freqLists with the lists for each frequency
        for el, freq in count.items():
            #add the element to the list of it's frequency
            #just freq if do len + 1 abov
            freqLists[freq-1].append(el)

        #run through the frequency lists and create list of k elements
        result = []
        for freqList in reversed(freqLists):
            for i in freqList:
                result.append(i)
                #putting it after, becausae k is at least 1 so will always need to do first one
                #and so avoids unnecessary check beforehand
                #check with len instead to avoid changing k when don't have to
                if len(result) == k: 
                    return result
        return result


        
        
