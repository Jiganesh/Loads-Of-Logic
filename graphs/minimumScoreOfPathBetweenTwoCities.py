# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

from typing import List
from collections import deque, defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        
        graph = defaultdict(list)
        weights = defaultdict()
        
        for u, v, i in roads:
            graph[u].append(v)
            graph[v].append(u)
            
            weights[(u,v)] = i
            weights[(v,u)] = i
        
        score = [float("inf") for i in range (n+1)]
        queue = deque([(1,float("inf"))])
        
        
        while queue:
            node, distance = queue.popleft()
            
            for children in graph[node]:
                
                w1 = weights[(node,children)]
                w2 = score[children]

                if w1 < w2:
                    queue.append([children, w1])
                score[children] = min(w1, w2)
                    
        return(min(score))
