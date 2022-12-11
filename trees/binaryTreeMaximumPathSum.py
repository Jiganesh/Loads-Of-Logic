# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = float("-inf")
        def helper(root):

            if root:
                left_sum = helper(root.left)
                right_sum = helper(root.right)

                left_sum = left_sum  if left_sum >=0 else 0
                right_sum = right_sum if right_sum >= 0 else 0

                self.maximum = max(self.maximum, left_sum + right_sum + root.val)
                return root.val + max(left_sum, right_sum)

            return 0

        helper(root)
        return self.maximum