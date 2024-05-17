#O(klogn) time complexity
#O(n) memory but probably worst because hashmap of size n, another list of size n with object creation overhead, and result list of size k
class Element:
    def __init__(self, el: int, freq: int):
        self.el = el
        self.freq = freq
    
    #custom comparator, key for using heap
    def __lt__(self, other):
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqlist = {}
        for i in nums:
            #increment by 1, with 0 as the default value
            freqlist[i] = freqlist.get(i, 0) + 1
        
        freqArray = []

        #go through the frequency list, and fill the array with elements representing each part
        for el, freq in freqlist.items():
            freqArray.append(Element(el, freq))

        #heap we will hold at size k 
        minheap = []
        
        for e in freqArray:
            #to make sure to fill heap from empty
            if len(minheap) < k:
                heapq.heappush(minheap, e)
            #if element's freq is less than min currently, point adding
            #only add if freq is more than the min
            #could alternatively add and then pop, but doing that everytime is more work than only popping and adding if need to
            elif e > minheap[0]:
                #pushes then pops smallest as efficiently as possible
                heapq.heappushpop(minheap, e)
        
        #will be of size k, and have the k biggest 
        return [element.el for element in minheap]
