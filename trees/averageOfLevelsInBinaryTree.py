# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Both solutions are O(n) time and O(n) space. 
    # The first solution is a BFS solution. 
    # The second solution is a DFS solution. The second solution is more elegant and easier to understand.
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        
        result = []
        
        while q :
            
            avg = sum([i.val for i in q]) / len(q)
            
            result.append(avg)
            
            q = [child for p in q for child in (p.left, p.right) if child]
            
        return result
    
    
    # Runtime: 90 ms, faster than 33.24% of Python3 online submissions for Average of Levels in Binary Tree.
    # Memory Usage: 17.1 MB, less than 8.79% of Python3 online submissions for Average of Levels in Binary Tree.
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        
        level_dictionary = defaultdict(list)
        
        def helper(root, level=0):
            
            if root:
                level_dictionary[level].append(root.val)
                
                helper(root.left, level+1)
                helper(root.right, level+1)
                
        helper(root)
        return [ sum(value)/len(value) for _ , value in level_dictionary.items()]
