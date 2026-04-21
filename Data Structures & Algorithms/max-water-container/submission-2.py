class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # Brute Force
        # maxAreaEvaluated = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         height = min(heights[i], heights[j])
        #         width = j-i
        #         area = width * height
        #         maxAreaEvaluated = max(maxAreaEvaluated, area)
        
        # return maxAreaEvaluated
        maxAreaEvaluated = 0
        l , r = 0, len(heights)-1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            maxAreaEvaluated = max(maxAreaEvaluated, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxAreaEvaluated