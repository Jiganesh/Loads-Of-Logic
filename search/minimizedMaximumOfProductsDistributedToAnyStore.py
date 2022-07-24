# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

from typing import List
import math

class Solution:
    # Runtime: 3295 ms, faster than 39.03% of Python3 online submissions for Minimized Maximum of Products Distributed to Any Store.
    # Memory Usage: 28.6 MB, less than 15.45% of Python3 online submissions for Minimized Maximum of Products Distributed to Any Store.
    
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
    
        l = 1
        r = max(quantities)
        
        def num_of_products (mid):
            return sum([math.ceil(i/mid) for i in quantities])
        
        
        while l< r:
            mid = (l+r)//2
            maximum = num_of_products(mid)
            
            if maximum > n:
                l=mid+1
            else:
                r= mid
            
                
        return l
    
    
    