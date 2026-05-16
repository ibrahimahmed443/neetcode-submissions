class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPointer, sellPointer = 0, 1
        while sellPointer < len(prices):
            if prices[sellPointer] <= prices[buyPointer]:
                buyPointer = sellPointer
                sellPointer = buyPointer + 1
            else:
                profit = prices[sellPointer] - prices[buyPointer]
                maxProfit = max(profit, maxProfit)
                sellPointer += 1

        return maxProfit
