# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
from typing import List


class Solution:
    
    # TC : O(NlogN)
    # SC : O(1)
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        left = 0
        right = len(nums)-1

        maximum = float("-inf")

        while left < right:
            pair = nums[left]+nums[right]
            maximum = max(pair, maximum)
            left+=1
            right-=1

        return maximum
    
    
'''
why not sort the array and then take the first and last element and add them to get the maximum sum ?

Please check the example - [4,1,5,1,2,5,1,5,5,4]

After sorting this array - [1,1,1,2,4,4,5,5,5,5] gives us 6 which is clearly not the maximum sum possible
It will be 4+4 = 8

'''

