# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

from typing import List
from itertools import accumulate
import bisect, operator

class Solution:
    
    # TC : O(N*log(N)+ Q*log(N))
    # SC : O(N+Q)
    
    # Runtime: 112 ms, faster than 80.00% of Python3 online submissions for Longest Subsequence With Limited Sum.
    # Memory Usage: 14.2 MB, less than 80.00% of Python3 online submissions for Longest Subsequence With Limited Sum.

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        prefix_sum = list(accumulate(nums, operator.add))
        
        return [bisect.bisect_right(prefix_sum, summation) for summation in queries]
    
