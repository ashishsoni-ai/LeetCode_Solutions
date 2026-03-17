class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            curr_profit = prices[i] - min_prices
            if curr_profit>profit:
                profit = curr_profit
            min_prices = min(min_prices,prices[i])
        return profit

        