# https://leetcode.com/problems/binary-tree-tilt/
# https://www.youtube.com/watch?v=h-Wo5TIzfjI

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Runtime: 65 ms, faster than 80.86% of Python3 online submissions for Binary Tree Tilt.
    # Memory Usage: 16.4 MB, less than 10.73% of Python3 online submissions for Binary Tree Tilt.
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def helper(root):
            
            if not root : return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            self.ans += abs(left - right)
            
            return left+right+root.val
        
        helper(root)
        return self.ans