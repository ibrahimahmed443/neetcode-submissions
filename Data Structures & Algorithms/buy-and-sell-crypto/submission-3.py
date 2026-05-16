class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPointer, sellPointer = 0, 1
        while sellPointer < len(prices):
            if prices[buyPointer] < prices[sellPointer]:  # is profitable?
                profit = prices[sellPointer] - prices[buyPointer]
                maxProfit = max(profit, maxProfit)
                sellPointer += 1
            else:
                buyPointer = sellPointer
                sellPointer = buyPointer + 1

        return maxProfit
