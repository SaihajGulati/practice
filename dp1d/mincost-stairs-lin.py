class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        one = 0
        two = 0
        # each one contains total cost to get to that stair
        for i in range(2, len(cost) + 1):
            temp = min(one + cost[i-1], two + cost[i-2])
            two = one
            one = temp

        return one
