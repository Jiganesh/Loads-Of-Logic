# https://leetcode.com/problems/course-schedule-iii/

import heapq
from typing import List

class Solution:
    # Runtime: 872 ms, faster than 62.47% of Python3 online submissions for Course Schedule III.
    # Memory Usage: 20 MB, less than 51.03% of Python3 online submissions for Course Schedule III.
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        total_time_spent =0
        heap = []
        for duration , lastDay in sorted(courses, key= lambda x: (x[1], x[0])) :
            total_time_spent +=duration
            heapq.heappush(heap, -duration)
            
            if total_time_spent > lastDay:
                total_time_spent += heapq.heappop(heap)
                
        return len(heap)
    
    