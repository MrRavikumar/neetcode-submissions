class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute Force
        # def calucalteHours(piles, hour):
        #     totalHours = 0
        #     for i in piles:
        #         totalHours += math.ceil(i/hour)
        #     return totalHours
        
        # maxVal = max(piles)
        # for i in range(1, maxVal+1):
        #     hr = calucalteHours(piles, i)
        #     if hr <= h:
        #         return i

        # return maxVal

        # Optimized
        maxPile = max(piles)
        ans = maxPile
        low, high = 1, maxPile
        ans = maxPile

        def calculateHours(piles, hour):
            totalHours = 0
            for bananas in piles:
                totalHours += math.ceil(bananas/hour)
            return totalHours

        while low <= high:
            mid = (low + high) // 2
            totalH = calculateHours(piles, mid)
            if totalH <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

