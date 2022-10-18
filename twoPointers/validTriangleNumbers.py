# https://leetcode.com/problems/valid-triangle-number/
from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        
        result = 0 
        for right in range (2, len(nums)):
            left, middle = 0 , right-1
            while left < middle:
                if nums[left]+nums[middle] > nums[right]:
                    result += middle-left
                    middle-=1
                else:
                    left+=1

        return result
