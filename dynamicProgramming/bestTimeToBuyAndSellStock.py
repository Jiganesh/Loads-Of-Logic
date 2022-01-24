# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Solution : https://www.youtube.com/watch?v=4YjEHmw1MX0


class Solution(object):
    
    
    #TC: O(N^2)
    # SC: O(1)
    
    # BruteForce : TLE
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum = 0
        
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                maximum = max(maximum, prices[j]-prices[i])
                    
        return maximum
            
    
    
    # TC: O(N)
    # SC: O(1)
    
    # Efficient
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        leastPriceOfStockSoFar = prices[0]
        profitMadeToday, overallProfit =0,  0
        
        for i in range(1,len(prices)):
            leastPriceOfStockSoFar = min(leastPriceOfStockSoFar, prices[i])
            profitMadeToday= prices[i]-leastPriceOfStockSoFar
            overallProfit= max(overallProfit, profitMadeToday)
            
        return overallProfit
    
print(Solution().maxProfit([7,1,2,5,6,4]))