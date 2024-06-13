class Solution:
    #T: O(m), where m is size of tasks and n is idle time
    #m because have to go through all tasks to fill heap and of course to schedule
    #would think would be m * n because in the worst case is all same letters with n idle time, then will run loop m * n times to get m * n time
    #BUT THE IF STATEMENT IS SUPER SMART
    #ALSO not O(mlogm) BECAUSE will have max one count per letter, and only 26 letters possible, so O(26) = O(1) to add to heap instead of O(logm)
    def leastInterval(self, tasks: List[str], n: int) -> int: 
        #gives hashmap of count of each letter
        count = Counter(tasks)
        #creating max heap (hence the negative) of the counts
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, timeAvailable]
        #if maxHeap, means have letters can schedule
        #if queue but not maxHeap, means there are still letters to schedule but have to do idle time for this slot
        while maxHeap or q:
            time += 1 #counter

            #if the maxHeap is empty, then are just waiting for the next one in queue's idle time
            #the next one in the queue is guaranteed to be first because it was the first one loaded AND ALL idle times are identital
            #so this is a shortcut to skip to that time
            #makes runtime O(m) not O(m * n)
            if not maxHeap:
                time = q[0][1]
            else: #heap has values, so have values can schedule
                #add one to the count (really subtract one, but is a maxHeap using negatives for python so opposite)
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: #still count of that letter left to schedule, put into queue because need to wait the idle time amount
                    q.append([cnt, time + n])
            if q and q[0][1] == time: #checing if q first so don't get index out of bounds when access
                #means just passed time needed to pass, so can add back to heap because can be scheduled starting next time
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
