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

# arr = [7,1,7,2,2,4]
# n = len(arr)
# stack = []
# maxArea = 0

# for i in range(n+1):
#     print("Iteration Number: ", i)
#     cur_height = arr[i] if i < n else 0
#     print("Current Height: ", cur_height)
#     while stack and (i == n or arr[stack[-1]] >= cur_height):
#         print()
#         height = arr[stack.pop()]
#         print("Height: ", height)
#         print("stack in while: ", stack)
#         if not stack:
#             width = i
#             print("width in if:", width)
#         else:
#             width = i - stack[-1] - 1
#             print("width in else:", width)
        
#         area = height * width
#         print("max ( maxArea: ",maxArea,", area: ",area," )")
        
#         maxArea = max(maxArea, area)
        
        
#     stack.append(i)
#     print("stack: ", stack)
#     print("===================================================")