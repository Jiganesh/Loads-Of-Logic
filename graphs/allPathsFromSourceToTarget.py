# https://leetcode.com/problems/all-paths-from-source-to-target/
from typing import List

class Solution:
        
    # TC : O(2^N)
    # SC : O(N^2)
    
    # Runtime: 98 ms, faster than 96.47% of Python3 online submissions for All Paths From Source to Target.
    # Memory Usage: 15.6 MB, less than 97.23% of Python3 online submissions for All Paths From Source to Target.
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)        
        result = []
        
        def helper(node, path=[0]):
            
            if node == n-1:
                result.append(path)
                return 
            
            for child in graph[node]:
                helper(child, path+[child])
                
        helper(0)
        return result
    
    # Recursive Solution Technique
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)

        def helper(graph, node=0):
            
            if node == n-1:
                return [[n-1]]
            
            ans = []
            for child in graph[node]:
                for path in helper(graph, child):
                    ans.append([node]+path)
            return ans
        
        return helper(graph)
    
    # TC : O(2^N)
    # SC : O(N^2)
    
    # One Liner Solution of above solution
    
    # Runtime: 150 ms, faster than 53.91% of Python3 online submissions for All Paths From Source to Target.
    # Memory Usage: 15.8 MB, less than 24.07% of Python3 online submissions for All Paths From Source to Target.
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        
        def helper(graph, node=0):
            
            if node == n-1:return [[n-1]]
            return [([node]+ path) for child in graph[node] for path in helper(graph, child)]
                    
        return helper(graph)