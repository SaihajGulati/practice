class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #T: O(n)
        #M: O(1)
        max_score = 0
        max_left = values[0] #bc if values[0] + 0 technically as max left of it when viewed by next
        #holds max values[i] + i score of all seen to left of where at

        for i in range(1, len(values)):
            right_score = values[i] - i #acting as j here
            max_score = max(max_score, max_left + right_score)
        
            left_score = values[i] + i #if was left here
            max_left = max(left_score, max_left) #update max_left 

        return max_score
        
