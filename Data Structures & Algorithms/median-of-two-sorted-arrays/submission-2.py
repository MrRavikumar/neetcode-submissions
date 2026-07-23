class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # # Brute Force
        # merged = []
        # i = 0
        # j = 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         merged.append(nums1[i])
        #         i = i + 1
        #     else:
        #         merged.append(nums2[j])
        #         j = j + 1
        
        # merged += nums1[i:]
        # merged += nums2[j:]

        # n = len(merged)
        # if n % 2 == 1:
        #     return merged[n // 2]
        # else:
        #     return (merged[n // 2 - 1] + merged[n // 2]) / 2.0

        # Optimized Approach 
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        n1 , n2 = len(nums1), len(nums2)
        low, high = 0, n1
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1
            
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r1 = float('inf') if cut1 == n1 else nums1[cut1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]
            
            if l1<=r2 and l2<=r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            
            if l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        return 0.0

