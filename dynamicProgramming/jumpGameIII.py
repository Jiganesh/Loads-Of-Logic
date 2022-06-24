# https://leetcode.com/problems/jump-game-iii/
from typing import List


class Solution:
    # Runtime: 342 ms, faster than 75.62% of Python3 online submissions for Jump Game III.
    # Memory Usage: 70 MB, less than 18.23% of Python3 online submissions for Jump Game III.
    
    # TC : O(N)
    # SC : O(N)
    
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = [0] * len(arr)
        def helper(position):
            
                
            if position<0 or position>len(arr)-1 :
                return False
            
            if visited[position]==1:
                return False
            
            if arr[position] == 0:
                return True
            
            visited[position] = 1
            return helper(position-arr[position]) or helper(position+arr[position])
        
        return helper(start)