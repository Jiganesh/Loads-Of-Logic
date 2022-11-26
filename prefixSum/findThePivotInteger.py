# https://leetcode.com/problems/find-the-pivot-integer/

from collections import accumulate
import operator

# Step 1 n = 8
# Step 2 nums = [0,1,2,3,4,5,6,7,8]
# Step 3 prefix_sum = [0,1,3,6,10,15,21,28,36]
# Step 4 find a point where prefix_sum[i] = prefix_sum[-1] - prefix_sum[i+1]
# Step 5 If not found, return -1 

class Solution:
    def pivotInteger(self, n: int) -> int:
        
        
        nums = [i for i in range (n+1)]
        prefix_sum = list(accumulate( nums,operator.add))
        
        last = prefix_sum[-1]
        
        for i in range (1, len(prefix_sum)):
            if last - prefix_sum[i] == prefix_sum[i-1]:
                return prefix_sum[i]-prefix_sum[i-1]
            
        return -1