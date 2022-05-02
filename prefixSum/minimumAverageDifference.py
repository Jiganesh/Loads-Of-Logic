# https://leetcode.com/problems/minimum-average-difference/

import math 
import operator
from itertools import  accumulate

class Solution:
    
    # Runtime: 1148 ms, faster than 25.00% of Python3 online submissions for Minimum Average Difference.
    # Memory Usage: 25.3 MB, less than 25.00% of Python3 online submissions for Minimum Average Difference.
    def minimumAverageDifference(self, nums) -> int:
        
        prefixSum = list(accumulate(nums, operator.add))
        
        minindex = [-1, float("inf")]
        for index  , i in enumerate(prefixSum):
            
            leftside = i
            numbersinleftside = index+1
            
            rightside = prefixSum[-1]-i
            numbersinrightside = len(prefixSum)-numbersinleftside if numbersinleftside < len(prefixSum) else 1
            
            l = math.floor(leftside/numbersinleftside)
            r = math.floor(rightside/numbersinrightside)
            
            if minindex[1] > abs(l-r):
                minindex = [index, abs(l-r)]
                
        return minindex[0]
        