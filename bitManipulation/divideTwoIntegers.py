# https://leetcode.com/problems/divide-two-integers/

class Solution(object):
    
    # Runtime: 19 ms, faster than 90.51% of Python online submissions for Divide Two Integers.
    # Memory Usage: 13.4 MB, less than 69.16% of Python online submissions for Divide Two Integers.
    
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        
        if dividend == divisor : return 1
        
        isPositive = (dividend <0 )== (divisor <0)
        
        dividend=abs(dividend)
        divisor=abs(divisor)

        q = 0
        while dividend >= divisor:
            bit = 0
            
            while(dividend >= (divisor<<(bit+1))):
                bit+=1
                
            q+= 1 <<(bit)
            dividend -= divisor<<bit
            
        return min( q if isPositive else -q, 2**31-1)