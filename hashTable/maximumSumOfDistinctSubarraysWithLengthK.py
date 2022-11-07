# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

                
        runningSum = 0  # Keeping Track of Window
        lookup_last_ind = defaultdict(lambda: -1)  # Key : Value pair of number and last seen index

        result = 0 # maximum subarray sum without duplicates

        index_of_duplicate_number = -1  # index of duplicate number


        for ind, num in enumerate(nums):

            runningSum += num     # Expanding Window, adding number

            if ind >= k : 
                runningSum-= nums[ind-k] # Decreasing window if its greater than given k size

            if ind - lookup_last_ind[num] < k: # check the duplicate number and make sure its not in range
                index_of_duplicate_number = max(index_of_duplicate_number, lookup_last_ind[num])  # record lastest index with duplicate

            if ind - index_of_duplicate_number >= k: # check if last_index of duplicate number is in k size
                result = max(result, runningSum)

            lookup_last_ind[num] = ind  # record last seen number

        return result
