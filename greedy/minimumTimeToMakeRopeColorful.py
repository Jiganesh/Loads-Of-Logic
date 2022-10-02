# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

from typing import List
import heapq


class Solution:
    
    # TC : O(nlogn)
    # SC : O(n)
    
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        colors = colors+"*"
        neededTime.append(-1)
        heap = []
        result = 0
        for ind , ch in enumerate(colors):

            if heap and heap[0][1]==ch:
                heapq.heappush(heap, (neededTime[ind], ch))
            else:

                while len(heap)>1:
                    result += heapq.heappop(heap)[0]
                
                heap = [(neededTime[ind], ch)]
        return result
    
    # TC : O(n)
    # SC : O(1)    
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        left = 0
        right = 0
        
        result = 0

        while left < len(colors):

            while right< len(colors) and colors[right]==colors[left]:
                right+=1

            maximum = float("-inf")

            while left<right:
                maximum = max(maximum, neededTime[left])
                left+=1
            
            result+=maximum
            
        return sum(neededTime)-result 