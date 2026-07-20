class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # Brute Force
        # if len(nums) == 0:
        #     return -1
        # for i in range(len(nums)):
        #     if nums[i] != target:
        #         continue
        #     return i
        
        # return -1

        # Optimized 
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low+high) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
        return -1



        