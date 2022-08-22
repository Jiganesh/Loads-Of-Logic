# https://leetcode.com/problems/power-of-two

class Solution:
    # Runtime: 60 ms, faster than 28.63% of Python3 online submissions for Power of Two.
    # Memory Usage: 13.8 MB, less than 53.53% of Python3 online submissions for Power of Two.
    def isPowerOfTwo(self, n: int) -> bool:
        
        # Condition 1 check if number is positive Natural Number -- > n > 0
        # Condition 2 check if there exist only one set bit --> n & (n-1)  == 0
        
        return n > 0 and (n&(n-1))==0