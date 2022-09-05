# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # Runtime: 53 ms, faster than 94.36% of Python3 online submissions for N-ary Tree Level Order Traversal.
    # Memory Usage: 16 MB, less than 94.71% of Python3 online submissions for N-ary Tree Level Order Traversal.
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root: return []
        
        result = []
        
        q = [root]
        
        while q:
            result .append([i.val for i in q if i])
            q = [child for p in q for child in (p.children) if child]
            
        return result
    
