class Solution:
    def findMin(self, nums: List[int]) -> int:
        # # Brute Force
        # minVal = float('inf')
        # for i in nums:
        #     minVal = min(minVal, i)
        
        # return minVal

        # Optimized
        low, high = 0, len(nums)-1
        while low<high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        return nums[low]

        