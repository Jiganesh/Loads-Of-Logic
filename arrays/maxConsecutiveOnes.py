# https://leetcode.com/problems/max-consecutive-ones/
from typing import List

class Solution:
    # TC : O(N)
    # SC : O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        result = count = 0

        for num in nums:
            if num == 1:
                count+=1
                result = max(result, count)
            else :
                count = 0

        return result