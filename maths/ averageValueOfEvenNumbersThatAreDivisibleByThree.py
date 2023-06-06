# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:

        count = 0
        sum = 0

        for num in nums:
            if num%6==0:
                sum+=num
                count+=1

        return sum//count if count else 0
