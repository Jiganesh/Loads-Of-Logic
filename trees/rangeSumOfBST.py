# https://leetcode.com/problems/range-sum-of-bst/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:


        self.result = 0
        def helper(root):
            if root:
                helper(root.left)
                self.result += root.val if low<=root.val<=high else 0
                helper(root.right)

        helper(root)
        return self.result