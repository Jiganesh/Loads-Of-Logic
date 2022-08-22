class Solution:

    # TC : O(log4n)
    # SC : O(1)
    
    # Runtime: 39 ms, faster than 82.22% of Python3 online submissions for Power of Four.
    # Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four.
    
    def isPowerOfFour(self, n: int) -> bool:
        x = 1

        while x <= n :
            if x==n:
                return True
            x = x<<2

        return False
    
    # TC : O(32)
    # SC : O(1)
    def isPowerOfFour(self, n: int) -> bool:
        
        # Condition 1 - The number is positive
        if n <=0:
            return False
        
        # Condition 2 - There should be only one bit present
        if n & (n-1) != 0:
            return False
        
        # Condition 3 - The one bit present should be at even place
        
        # 00001  --> 1   bit present at 0
        # 00100  --> 4   bit present at 2
        # 10000  --> 16  bit present at 4
        
        for bit_location in range (0, 32): # 32-bit Integer
            
            mask  = 1 << bit_location
            if bit_location%2==0 and (mask & n) != 0:
                return True
            
        return False
    # One liner
    
    # TC : O(1)
    # SC : O(1)
    
    # Runtime: 22 ms, faster than 99.91% of Python3 online submissions for Power of Four.
    # Memory Usage: 13.8 MB, less than 95.34% of Python3 online submissions for Power of Four.
    def isPowerOfFour(self, n: int) -> bool:
        
        return n>0 and (n & (n-1)) == 0  and  (0b1010101010101010101010101010101 & n) !=0
    
    