class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #Final Solution -- T: O(n) M: O(1)
        
        #found this solution by drawing tree and dynamic programming kinda like first climbing stairs neet video NOT the video for this problem
        #bc using cost in for loop
        one = 0
        two = 0

        #has to go backwards
        #reversed means biggest is still excluded, so this goes from last index of cost (len(cost)-1) to 0th index
        for i in reversed(cost):
            temp = min(i + one, i + two)
            two = one
            one = temp

        #ends with last one being the 0th cost index, so need to min 0th and 1st to get true min since can start at either one
        return min(one, two)
