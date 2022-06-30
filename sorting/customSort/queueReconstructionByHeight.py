# https://leetcode.com/problems/queue-reconstruction-by-height/

from typing import List

class Solution:
    
    # Runtime: 112 ms, faster than 80.90% of Python3 online submissions for Queue Reconstruction by Height.
    # Memory Usage: 14.6 MB, less than 14.52% of Python3 online submissions for Queue Reconstruction by Height.
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        def custom_sort(x):
            return -x[0], x[1]
        
        people.sort(key = custom_sort)
        
        queue = []
        for height, taller in people:
            queue.insert(taller, [height, taller])
            
        return queue