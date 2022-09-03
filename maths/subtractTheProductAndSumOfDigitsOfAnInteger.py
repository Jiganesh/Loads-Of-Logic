# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    
    # Runtime: 52 ms, faster than 37.18% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
    # Memory Usage: 13.8 MB, less than 53.78% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.

    def subtractProductAndSum(self, n: int) -> int:
        
        product = 1
        summation = 0
        
        while n :
            product *= (n% 10)
            summation += (n%10)
            
            n//=10
            
        return product-summation
