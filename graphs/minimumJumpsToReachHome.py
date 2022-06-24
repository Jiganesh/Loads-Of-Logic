from typing import List
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        def BFS (forbidden,root, a, b , x):
            queue = deque()
            seen = set()
            
            queue.append((root, False))
            seen.add((root, False))
            
            ans = 0
            
            while queue:
                
                for _ in range (len(queue)):
                    current_position, is_backward = queue.popleft()
                    
                    if current_position ==x:
                        return ans
                    
                    next_position = current_position + a
                    node = (next_position, False)
                    if next_position not in forbidden and next_position < 2000+max(a, b) and node  not in seen:
                        queue.append(node)
                        seen.add(node)
                        
                    
                    if not is_backward: #As we are not supposed to go backward twice
                        next_position = current_position-b
                        node = (next_position, True)
                        if next_position not in forbidden and next_position>=0 and node not in seen:
                            queue.append(node)
                            seen.add(node)
                        
                ans+=1
                
        return BFS(forbidden, 0, a , b , x)
                
print(Solution().minimumJumps([14,4,18,1,15], 3, 15, 9))
                        