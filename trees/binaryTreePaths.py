# https://leetcode.com/problems/binary-tree-paths/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Runtime: 27 ms, faster than 98.66% of Python3 online submissions for Binary Tree Paths.
    # Memory Usage: 14 MB, less than 29.37% of Python3 online submissions for Binary Tree Paths.
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.result = []
        
        
        def helper(root, array):
            
            
            if not root.left and not root.right :
                self.result.append("->".join(array[:]))
            
            for i in (root.left, root.right):
                if i : 
                    helper(i, array+[str(i.val)])
                    
        helper(root, [str(root.val)])
        return self.result 
                    
                    
        