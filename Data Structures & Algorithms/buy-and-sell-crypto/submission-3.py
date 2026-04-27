class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        # # Brute Force
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         maxProfit = max(maxProfit, profit)
        # return maxProfit

        # Optimal:
        minPrice = float('inf')
        for price in prices:
            minPrice = min(price, minPrice)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit
        