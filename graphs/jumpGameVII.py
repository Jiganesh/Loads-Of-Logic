# https://leetcode.com/problems/jump-game-vii/
# https://www.youtube.com/watch?v=v1HpZUnQ4Yo
from collections import deque


class Solution:
    
    # Runtime: 514 ms, faster than 69.05% of Python3 online submissions for Jump Game VII.
    # Memory Usage: 18 MB, less than 59.33% of Python3 online submissions for Jump Game VII.
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        def bfs (root):
            
            q = deque([root])
            farthest = 0
            n = len(s)-1
            
            while q:
                index = q.popleft()
                
                start = max(index+minJump, farthest+1) # for optimization
                end = min(index+maxJump , n)+1       # for logic
                
                for i in range (start ,end):
                    if s[i] == "0":
                        q.append(i)
                        if i==n : return True
                        
                farthest = index+maxJump

            return False
        
        return bfs(0)
                    
                    
            
                 
        return bfs(0)
            