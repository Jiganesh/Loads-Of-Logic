# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

from collections import defaultdict
import bisect


class Solution:
    def countRectangles(self, rectangles, points) :
        
        sorted_heights = defaultdict(list)
        for length, height in rectangles:
            sorted_heights[height].append(length)
            
        for h in sorted_heights:
            sorted_heights[h].sort()
    
        result = []
        for point in points:
            l, h = point
            count = 0
            for height in sorted_heights:
                if height>=h:
                    count += len(sorted_heights[height])-bisect.bisect_left(sorted_heights[height], l)
                    
            result.append(count)
        return result 
            