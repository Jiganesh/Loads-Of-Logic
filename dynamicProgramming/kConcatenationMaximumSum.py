# https://leetcode.com/problems/k-concatenation-maximum-sum/

from typing import List
class Solution:
    
    # Runtime: 956 ms, faster than 24.64% of Python3 online submissions for K-Concatenation Maximum Sum.
    # Memory Usage: 28.4 MB, less than 66.18% of Python3 online submissions for K-Concatenation Maximum Sum.
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        def kadane_algorithm(arr):
            
            res = curr = 0
            for i in range (len(arr)):
                curr = max(curr+arr[i], arr[i])
                res = max(res, curr)
            return res
        
        MOD = (10**9)+7
        
        if k==1:
            return kadane_algorithm(arr) % MOD
        else :
            return (max(sum(arr), 0) * (k-2) + kadane_algorithm(arr*2)) % MOD