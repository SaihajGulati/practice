class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        originTo = {}
        #there by default
        itinerary = ["JFK"]


        #T: O(E^2) = O(n^2) because though dfs is O(V+E) and here E dominates because could be multiple destinations for a origin, backtracking means could go through all of them each time so O(E*E) 
        # M: O(V+E) which is adjacency list and here simplifies to O(E) = O(n) bc of adjacency list storing all tickets essentially and bc of recrusive call stack at once having up to E bc runs, checks all till end, and then continues

        #puts all the tickets in sorted order automatically when put into deque
        tickets.sort()

        #fills hash map with all possible destinations for each origin
        for origin, dest in tickets:
            if (origin not in originTo):
                #because could have duplicates so set won't work
                originTo[origin] = deque()
            originTo[origin].append(dest)
        
        def dfs(origin):
            if len(itinerary) == len(tickets) + 1:
                return True
            #if did not get valid itineary as checked above, but
            #reached an "origin" which was never specified as an origin, means we reached the end of this path because we're stuck
            #or if this was an origin at some point, but we've ran out of tickets for it, also false
            elif origin not in originTo or len(originTo[origin]) == 0: 
                return False

            #will be copy, which need so that can remove from original set without losing the values needed
            #can't use slice hack to save a bit of memory here because deque doesn't allow list slicing
            tempDests = list(originTo[origin])

            #range is a function that is called once so will only check length at first
            #need to do length times to go through each in this list of dests
            for dest in tempDests:
                #always popleft because this will be removed and added to end so next one is alphabetically first one
                originTo[origin].popleft()
                itinerary.append(dest)
                #dest becomes new origin in dfs if get true back
                if (dfs(dest)):
                    return itinerary
                #else was false, so move on with a reset
                itinerary.pop()
                originTo[origin].append(dest)

        return dfs("JFK")
