class Solution:
    def trap(self, height: List[int]) -> int:
        # Two Pointers Approach
        lmax = rmax = total = 0
        l, r = 0, len(height)-1
        while l < r:
            if height[l] < height[r]:
                if lmax > height[l]:
                    total += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if rmax > height[r]:
                    total += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1
        
        return total

        