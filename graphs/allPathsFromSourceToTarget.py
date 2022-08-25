# https://leetcode.com/problems/all-paths-from-source-to-target/
from typing import List

class Solution:
    
    # Runtime: 98 ms, faster than 96.47% of Python3 online submissions for All Paths From Source to Target.
    # Memory Usage: 15.6 MB, less than 97.23% of Python3 online submissions for All Paths From Source to Target.
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        graph = dict(enumerate(graph))
        
        result = []
        
        def helper(node, path=[0]):
            
            if node == n-1:
                result.append(path)
                return 
            
            for child in graph[node]:
                helper(child, path+[child])
                
        helper(0)
        return result