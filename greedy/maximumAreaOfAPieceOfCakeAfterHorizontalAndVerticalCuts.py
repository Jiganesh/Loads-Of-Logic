from typing import List

# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution:
    
    # TC: O(h*log h + v*log v)
    # SC : O(V+H)
    
    # Runtime: 415 ms, faster than 64.46% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
    # Memory Usage: 26.7 MB, less than 77.43% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
                
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        max_v = max(verticalCuts[0], w-verticalCuts[-1])
        

        for i in range (1, len(horizontalCuts)):
            max_h = max(max_h , horizontalCuts[i]-horizontalCuts[i-1])
    
            
        for i in range(1, len(verticalCuts)):
            max_v = max(max_v, verticalCuts[i]-verticalCuts[i-1])
            
        return (max_h * max_v) % (10**9+7)