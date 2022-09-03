# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

from typing import List
import math

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        result = set()
        def helper(number):
                
            if int(math.log10(number))+1 == n:
                result.add(number)
                return
            
            if int(math.log10(number))+1 > n:
                return 
            
            last_digit = number%10
            if 0<=last_digit-k<=9:
                new_number = number*10 + (last_digit-k)
                helper(new_number)
            if 0<=last_digit+k<=9:
                new_number = number*10 + (last_digit+k)
                helper(new_number)
                
        for i in range(1, 10):
            helper(i)
        
        return result 
