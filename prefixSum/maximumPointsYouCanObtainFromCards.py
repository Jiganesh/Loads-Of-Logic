# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

import operator
from itertools import accumulate
from typing import List


class Solution:

    # Runtime: 628 ms, faster than 40.42% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
    # Memory Usage: 27.6 MB, less than 17.59% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        min_subarray_len = len(cardPoints)-k
        prefix_sum = [0] + list(accumulate(cardPoints, operator.add))
        
        i = 0 
        minimum_subarray_sum = float("inf")
        
        while i+min_subarray_len < len(prefix_sum):
            minimum_subarray_sum = min(minimum_subarray_sum,   prefix_sum[i+min_subarray_len] - prefix_sum[i])
            i+=1
        
        return prefix_sum[-1] - minimum_subarray_sum
    
    