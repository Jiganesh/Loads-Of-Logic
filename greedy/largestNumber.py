# https://www.youtube.com/watch?v=SzzSwvQfKyk
# https://leetcode.com/problems/largest-number/

from typing import List
from functools import cmp_to_key


class Solution:
    
    # Runtime: 42 ms, faster than 90.87% of Python3 online submissions for Largest Number.
    # Memory Usage: 14 MB, less than 21.15% of Python3 online submissions for Largest Number.
    def largestNumber(self, nums: List[int]) -> str:
        
        def custom_sort(a, b):
            print(a, b)
            
            #  2 and 10
            #  102 < 210 ?
            if a+b < b+a : return 1     # if a+b < b+a return 1 means 2 should appear first
            
            #  102 > 210
            if a+b > b+a : return -1    # if a+b > b+a return -1 means 10 should appear first
            return 0
        
        return str(int("".join(sorted(map(str, nums), key = cmp_to_key(custom_sort)))))