#O(kn) time complexity, O(n) memory complexity with only one hashmap of size n and one result list of size k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqlist = {}
        for i in nums:
            #increment by 1, with 0 as the default value
            freqlist[i] = freqlist.get(i, 0) + 1
        
        result = []
        #do process to find max k times for k most freq elements
        for i in range(k):
            topEl = -1
            topFreq = -1
            for el, freq in freqlist.items():
                if freq > topFreq:
                    topFreq = freq
                    topEl = el
            #once get here, have element remaining with top frequency
            result.append(topEl)
            #remove it so that next most one can be found next time
            del freqlist[topEl]
        return result
