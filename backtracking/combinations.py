# https://leetcode.com/problems/combinations/

from typing import List


class Solution:
    # Runtime: 815 ms, faster than 15.53% of Python3 online submissions for Combinations.
    # Memory Usage: 15.9 MB, less than 50.01% of Python3 online submissions for Combinations.

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.result = []
        def helper(array , index, k, n ):
            
            if len(array)==k:
                self.result.append(array[:])
                
            
            for i in range (index, n):
                helper(array+[i+1], i+1, k, n)
        
        helper([], 0, k, n)
        return self.result
    
        