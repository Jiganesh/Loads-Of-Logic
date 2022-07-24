# https://leetcode.com/problems/minimum-area-rectangle/

from typing import List

class Solution:
    
    # Runtime: 2857 ms, faster than 5.03% of Python3 online submissions for Minimum Area Rectangle.
    # Memory Usage: 14 MB, less than 99.83% of Python3 online submissions for Minimum Area Rectangle.
    
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        hashset = set(map(tuple, points))
        
        area = float("inf")
        for point1 in hashset:
            for point2 in hashset:
                
                x1, y1 = point1
                x2, y2 = point2
                
                if x1 < x2 and y1 < y2 and (x1, y2) in hashset and (x2, y1) in hashset:
                    area = min(area, (x2-x1)  *  (y2 -y1))
                    
        return area != float("inf") and area or 0