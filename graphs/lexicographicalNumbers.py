# https://leetcode.com/problems/lexicographical-numbers/
from typing import List

class Solution:
    # Runtime: 634 ms, faster than 5.13% of Python3 online submissions for Lexicographical Numbers.
    # Memory Usage: 22.4 MB, less than 31.93% of Python3 online submissions for Lexicographical Numbers.
    def lexicalOrder(self, n: int) -> List[int]:

        result = []
        
        def helper(digit):
            
            num_digit = int(digit)
            
            if 0 < num_digit <= n:
                result.append(num_digit)
                for next_digit in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    helper(digit+next_digit)
    
        for start in  ("1", "2", "3", "4", "5", "6", "7", "8", "9") :
            helper(start)                
        
        return result