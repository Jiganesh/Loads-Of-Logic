# https://leetcode.com/problems/reachable-nodes-with-restrictions/

from typing import List
from collections import defaultdict


class Solution:
    # TC : O(N)
    # SC: O(N) 
        
    
    # Runtime: 2947 ms, faster than 14.29% of Python3 online submissions for Reachable Nodes With Restrictions.
    # Memory Usage: 137.8 MB, less than 28.57% of Python3 online submissions for Reachable Nodes With Restrictions.
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        node_reached = set()
        def dfs(node):
            
            if not visited[node]:
                
                visited[node]=True
                node_reached.add(node)
                
                for child in graph[node]:
                    dfs(child)
                    
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False]*n
        for node in restricted:
            visited[node]=True
        
        dfs(0)
        
        return len(node_reached)
                
        
        