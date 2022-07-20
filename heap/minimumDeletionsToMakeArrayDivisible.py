
import heapq
from typing import List

# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

class Solution:
    
    # Runtime: 1877 ms, faster than 11.11% of Python3 online submissions for Minimum Deletions to Make Array Divisible.
    # Memory Usage: 29.9 MB, less than 100.00% of Python3 online submissions for Minimum Deletions to Make Array Divisible.

    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        def gcd (a, b):
            if b == 0 : return a
            else : return gcd(b, a%b)

        gcd_num = numsDivide[0]
        for i in numsDivide:
            gcd_num = gcd(gcd_num, i)
        
        heap = nums
        heapq.heapify(heap)
            
        count = 0
        
        while heap :
            
            val = heapq.heappop(heap)
            if gcd_num%val==0: return count
            count+=1
            
        return count if count<len(nums) else -1