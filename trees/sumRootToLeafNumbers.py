# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.sum = 0
        def helper(root, summation = 0):

            if root:

                if not root.left and not root.right:
                    self.sum += summation*10 + root.val
                    return 
                
                helper(root.left, summation*10 + int(root.val))
                helper(root.right, summation*10 +int(root.val))

                
            return 0

        helper(root)
        return self.sum