# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from typing import List

class Solution:
    
    # Runtime: 1222 ms, faster than 94.27% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
    # Memory Usage: 52.7 MB, less than 33.89% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        result = []
        hasInorder = set([e[1] for e in edges])
        
        for edge in range (n):
            if edge not in hasInorder:
                result.append(edge)
                
        return result 
    
    # One Liner not as efficient as above solution
    
    # Runtime: 2895 ms, faster than 5.05% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
    # Memory Usage: 52.1 MB, less than 84.86% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
    
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        return (list( set(range(n)) - set([e2 for e1, e2 in edges])   ))