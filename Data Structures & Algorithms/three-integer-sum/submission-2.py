class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # Brute Force
        # result = set()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             summation = nums[i]+nums[j]+nums[k]
        #             if summation == 0:
        #                 triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 result.add(triplet)
        
        # res = [list(t) for t in result]
        # return res
        
        # Optimized: Two Pointer Apporach 
        result = []
        target = 0
        sortedNums = sorted(nums)
        for i in range(len(sortedNums)):
            if i>0 and sortedNums[i] == sortedNums[i-1]:
                continue
            j, k = i+1, len(sortedNums)-1
            while j < k:
                sumation = sortedNums[i]+sortedNums[j]+sortedNums[k]
                if sumation < target:
                    j += 1
                elif sumation > target: 
                    k -= 1
                else:
                    result.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    while j<k and sortedNums[j] == sortedNums[j+1]:
                        j += 1
                    while k>j and sortedNums[k] == sortedNums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return result