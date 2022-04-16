# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

class Solution:
    
    
    # Runtime: 3520 ms, faster than 16.67% of Python3 online submissions for Number of Ways to Buy Pens and Pencils.
    # Memory Usage: 57.2 MB, less than 16.67% of Python3 online submissions for Number of Ways to Buy Pens and Pencils.
    
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        def helper(amount, cost1, cost2):
            dp = [0]*(amount+1)
            dp[0]=1

            for i in [cost1, cost2]:
                for j in range(1, amount+1):
                    if i <=j:
                        dp[j] = dp[j]+dp[j-i]
                        
            return sum(dp)

        return helper(total, cost1, cost2)
    
    # Runtime: 959 ms, faster than 100.00% of Python3 online submissions for Number of Ways to Buy Pens and Pencils.
    # Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Number of Ways to Buy Pens and Pencils.
    
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:    
    
        result = 0
        pens =0
        
        while pens * cost1 <= total:
            
            result+= (total-(pens*cost1))//cost2+1
            pens+=1
            
        return result
            
    
    
    
