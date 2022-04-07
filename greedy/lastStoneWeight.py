# https://leetcode.com/problems/last-stone-weight/

import heapq
import bisect


class Solution(object):
    
    # Submitted by Jiganesh
    
    # TC : O(N*NLogN)
    # SC : O(1)
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
        
    # Approach 2: Using a Max Heap [Accepted]
    def lastStoneWeight(self, A):
        h = [-x for x in A]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]
    
    
    # Approach 3: Using bisect Sort [Accepted]    
    def lastStoneWeight(self, stones):
        
        stones.sort()

        while len(stones)>1:
            x = stones.pop()
            y = stones.pop()
            if x != y : bisect.insort(stones, x-y)

        return stones[0] if stones else 0
                        