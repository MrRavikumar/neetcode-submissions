class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        stack = []
        for i in range(n + 1):
            cur_height = heights[i] if i < n else 0
            while (stack and (i == n or heights[stack[-1]] >= cur_height )):
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea