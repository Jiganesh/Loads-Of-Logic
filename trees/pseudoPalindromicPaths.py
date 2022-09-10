# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

from typing import  Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Runtime: 877 ms, faster than 94.69% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
    # Memory Usage: 85.1 MB, less than 72.81% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        def helper(root, bit_tracker):
            
            if root:
        
                bit_tracker[root.val]^=1
                
                if not ( root.right or root.left):
                    self.result += sum(bit_tracker)<=1
                    
                helper(root.left, bit_tracker)
                helper(root.right, bit_tracker)
                bit_tracker[root.val]^=1
            
        helper(root, [0]*10)
        return self.result 
        