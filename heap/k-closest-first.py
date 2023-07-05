class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        #the distance is from 0,0 so invisible -0 in each inside paren
        return sqrt((self.x)**2 + (self.y)**2) < sqrt((other.x)**2 + (other.y)**2)

    def listify(self):
        return [self.x, self.y]

class Solution:
  #since ends up nlogn bc of separate pushes, is not helping to use heap as this is same time complexity as any good sort algorithm
    #but would be valid first attempt, and then could explain that, and then say i wnt to be able to make use of O(n)ness of heapify, so what if we could...
    #and then try approach where change to list and then heapify
  #T:O(nlogn) M: O(n)
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        #will populate min heap sorted by distance
        #x, y strat here is cracked
        #O(nlogn) operation
        for x, y in points:
            heapq.heappush(minHeap, Point(x, y))
        
        return [heapq.heappop(minHeap).listify() for i in range (0, k)]
