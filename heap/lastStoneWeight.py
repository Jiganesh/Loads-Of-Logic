# https://leetcode.com/problems/last-stone-weight/KW

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>=2:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            
            if y-x :stones.append(y-x)
        
        if stones:
            return stones[-1]
        else:
            return 0
        
    
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        h = [-ele for ele in stones]
        heapq.heapify(h)
        
        while len(h)>1:
            heapq.heappush(h, (heapq.heappop(h)- heapq.heappop(h)))
            
        return -h[0]