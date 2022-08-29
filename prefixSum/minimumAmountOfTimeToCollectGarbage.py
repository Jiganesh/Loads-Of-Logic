# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/


from typing import List
from itertools import accumulate
import operator
from collections import Counter


class Solution:
    
    # Runtime: 2403 ms, faster than 25.00% of Python3 online submissions for Minimum Amount of Time to Collect Garbage.
    # Memory Usage: 36.3 MB, less than 75.00% of Python3 online submissions for Minimum Amount of Time to Collect Garbage.

    # TC: O(garbage*house + travel)
    # SC : O(N)
    
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        prefix_sum_travel = [0]+list(accumulate(travel, operator.add))
        
        count_p = count_g = count_m = 0
        ind_p = ind_g = ind_m = 0
        
        for ind, garbage_at_house in enumerate(garbage):
            
            lookup = Counter(garbage_at_house)
            
            if lookup["G"]:
                count_g+= lookup["G"]
                ind_g = ind
                
            if lookup["P"]:
                count_p+= lookup["P"]
                ind_p = ind
                
            if lookup["M"]:
                count_m+= lookup["M"]
                ind_m = ind
        
        return count_g + count_m + count_p + prefix_sum_travel[ind_g] + prefix_sum_travel[ind_m]+ prefix_sum_travel[ind_p]
    