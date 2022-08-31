# https://leetcode.com/problems/keys-and-rooms/

from typing import List

class Solution:
    
    # DFS Solution
    
    # TC: O(N)
    # SC : O(N)
    
    # Runtime: 93 ms, faster than 67.05% of Python3 online submissions for Keys and Rooms.
    # Memory Usage: 14.9 MB, less than 12.24% of Python3 online submissions for Keys and Rooms.
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        n = len(rooms)
        visited = [False]*n
        
        def helper(node):
            
            if visited[node] == False:
                visited[node]=True
                
                for child in rooms[node]:
                    helper(child)
        
        helper(0)
        
        for room in range(n):
            if visited[room]==False:
                return False
        return True