class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force
        maxAreaEvaluated = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j])
                width = j-i
                area = width * height
                maxAreaEvaluated = max(maxAreaEvaluated, area)
        
        return maxAreaEvaluated