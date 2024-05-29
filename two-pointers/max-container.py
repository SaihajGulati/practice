class Solution:
  #T: O(n)
  #M: O(1)
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while (l < r):
            area = (r - l) * min(heights[r], heights[l])
            max_area = max(area, max_area)
            if heights[l] >= heights[r]: 
                r -= 1
            else: 
                l += 1
        return max_area
        
