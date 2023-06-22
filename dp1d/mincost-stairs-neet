def minCostClimbingStairs(self, cost: List[int]) -> int:
      #this is the way in the neetcode video, where he rewrites the cost array instead of having two variables which is valid as well
      #saves some code in for loop and before, but makes for loop condition wack
      #this means goes from 3rd to last index to 0th since -1 is exclusive, and subtracts 1 each time
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
