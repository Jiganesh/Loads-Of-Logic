#  https://leetcode.com/problems/coin-change-2/

class Solution(object):
    
    
    # TC  : O(N*M)
    # SC : O(N)
    
    # Runtime: 180 ms, faster than 61.45% of Python online submissions for Coin Change 2.
    # Memory Usage: 13.8 MB, less than 48.79% of Python online submissions for Coin Change    2.
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for i in range (amount +1)]
        dp[0]=1
        
        for  coin in coins:
            for  currentAmount in range(1,amount+1):
                if coin <= currentAmount:
                    dp[currentAmount] =dp[currentAmount]+dp[currentAmount-coin]
                    
        return dp[amount]