# https://leetcode.com/problems/find-subarrays-with-equal-sum/

from typing import List

class Solution:
    
    # One Liner
    
    def findSubarrays(self, nums: List[int]) -> bool:
        arr =[sum(nums[i:i+2]) for i in range(len(nums)-1)]
        return len(arr) != len(set(arr))
    
    # Optimized Solution
    
    # Runtime: 48 ms, faster than 80.00% of Python3 online submissions for Find Subarrays With Equal Sum.
    # Memory Usage: 14 MB, less than 60.00% of Python3 online submissions for Find Subarrays With Equal Sum.
    
    def findSubarrays(self, nums: List[int]) -> bool:
        
        runningSum = 0
        n = len(nums)
        
        for ind in range(n):
            nums[ind] = nums[ind] +runningSum
            runningSum = nums[ind]
            
        prev = 0
        lookup_hashset = set()
        
        for i in range (1, n):
                    
            sum_of_pair = nums[i]-prev
            
            if sum_of_pair in lookup_hashset:
                return True
            
            lookup_hashset.add(sum_of_pair)
            prev = nums[i-1]
            
        return False
            
            