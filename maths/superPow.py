# https://leetcode.com/problems/super-pow/

from typing import List



# CRUX :  For example for a5347, the above computes a5, then a53, then a534, and then finally a5347. 
# And a step from one to the next can be done like a5347 = (a534)10 * a7.


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result = 1
        mod = 1337
        
        for i in b:
            
            result = pow(result, 10 , mod) * pow (a, i, mod)
            result %= mod
            
        return result 
            
    
    def superPow(self, a, b):
        return pow(a, b.pop(), 1337) * pow(self.superPow(a, b), 10, 1337) % 1337 if b else 1
    
    