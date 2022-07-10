# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

from fractions import Fraction
from collections import Counter
from typing import List


class Solution:
    # Runtime: 5271 ms, faster than 5.34% of Python3 online submissions for Number of Pairs of Interchangeable Rectangles.
    # Memory Usage: 70.1 MB, less than 46.18% of Python3 online submissions for Number of Pairs of Interchangeable Rectangles.
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        pairs = 0
        countPairs = Counter()
        
        for numerator , denominator in rectangles:
            
            num_den = Fraction(numerator, denominator)
            pairs += countPairs[num_den]
            countPairs[num_den] +=1
            
        return pairs
        
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        freq = Counter(w/h for w, h in rectangles)
        return sum(v*(v-1)//2 for v in freq.values())

