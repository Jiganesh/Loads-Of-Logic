# https://leetcode.com/problems/find-closest-number-to-zero/

class Solution:
    
    # Runtime: 176 ms, faster than 83.33% of Python3 online submissions for Find Closest Number to Zero.
    # Memory Usage: 14.2 MB, less than 16.67% of Python3 online submissions for Find Closest Number to Zero.
    def findClosestNumber(self, nums):
        
        def sortedfunction(n):
            return (abs(n-0),-n) 
        
        return sorted(nums, key = sortedfunction)[0]
        