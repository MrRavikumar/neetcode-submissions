class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force
        if len(nums) == 0:
            return -1
        for i in range(len(nums)):
            if nums[i] != target:
                continue
            return i
        
        return -1

        