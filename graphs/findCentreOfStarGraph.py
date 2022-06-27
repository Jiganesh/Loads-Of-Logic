# https://leetcode.com/problems/find-center-of-star-graph/

from typing import List
from collections import defaultdict

class Solution:
    # Runtime: 2003 ms, faster than 5.02% of Python3 online submissions for Find Center of Star Graph.
    # Memory Usage: 49.8 MB, less than 68.91% of Python3 online submissions for Find Center of Star Graph.
    def findCenter(self, edges: List[List[int]]) -> int:
    
        graph = defaultdict(int)
        
        for u, v  in edges:
            graph[u]+=1
            graph[v]+=1
            
        n = len(graph)
        
        for key, values in graph.items():
            if values==n-1:
                return key
            
    # Runtime: 2003 ms, faster than 5.02% of Python3 online submissions for Find Center of Star Graph.
    # Memory Usage: 49.8 MB, less than 68.91% of Python3 online submissions for Find Center of Star Graph.
    
    def findCenter(self, edges: List[List[int]]) -> int:
        
        s = set()
        
        for u, v in edges:
            if u in s:
                return u
            if v in s :
                return v
            s.add(u)
            s.add(v)
            
    # One Liner
    def findCenter(self, edges: List[List[int]]) -> int:
        
        return (set(edges[0])&set(edges[1])).pop()
    
    # Best Solution
    # TC : O(1)
    # SC : O(1)
        
    def findCenter(self, e):
        return e[0][e[0][1] in e[1]]

        