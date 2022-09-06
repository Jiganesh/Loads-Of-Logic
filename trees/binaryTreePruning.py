# https://leetcode.com/problems/binary-tree-pruning/

from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Runtime: 62 ms, faster than 19.19% of Python3 online submissions for Binary Tree Pruning.
    # Memory Usage: 13.8 MB, less than 68.92% of Python3 online submissions for Binary Tree Pruning.
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(root):
            
            if not root:
                return False
            
            left = helper(root.left) 
            right = helper(root.right)
            
            if left == False: root.left = None
            if right == False : root.right = None
                
            return left or right or root.val == 1
        
        return root if helper(root) else None
