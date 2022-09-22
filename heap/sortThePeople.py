# https://leetcode.com/problems/sort-the-people/

from typing import List
import heapq

class Solution:
    
    # Runtime: 255 ms, faster than 55.01% of Python3 online submissions for Sort the People.
    # Memory Usage: 14.3 MB, less than 89.95% of Python3 online submissions for Sort the People.
    
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        heights = list(map(lambda x : -x, heights))
        d = list(zip(heights, names))
        heapq.heapify(d)
        r = []
        while d:
            r.append(heapq.heappop(d)[1])
        return r
        
    # reduced space for List     
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        d = list(zip(heights, names))
        heapq.heapify(d)
        r = []
        while d:
            r.append(heapq.heappop(d)[1])
        r.reverse()
        return r
    
    # One Liner
    
    # Runtime: 214 ms, faster than 69.68% of Python3 online submissions for Sort the People.
    # Memory Usage: 14.4 MB, less than 89.95% of Python3 online submissions for Sort the People.
    
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        return [name for height , name in  sorted(zip(heights, names), reverse = True)]    