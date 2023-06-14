class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #you can use - sign to negate something in any language apparently, but is hella unclear so just use -1 in future
        #python magic, needed bc heaps are only minheaps in python and so this allwos for maxHeap
        stones = [-i for i in stones]

        heapq.heapify(stones)

        while (len(stones) > 1):
            biggest = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if (biggest != second):
                heapq.heappush(stones, -1 * (biggest-second))

        #gneius way to handle null case, because if list is empty, leads to returning 0 as need to, and if not empty, adds to end of list so no harm
        stones.append(0)
        #if get here, only one stone left but need to remember to make it positive
        return -stones[0]
