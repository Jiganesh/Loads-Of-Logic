# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        last = prices[0]
        result = 0

        for ind , price in enumerate(prices):

            if ind != 0 and prices[ind-1]< price:
                result += price-last
            last = price

        return result
