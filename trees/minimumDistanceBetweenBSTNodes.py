# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        self.array = []
        def helper(root):
            if root:
                helper(root.left)
                self.array.append(root.val)
                helper(root.right)
            return 0

        result = float("inf")
        helper(root)
        for i in range (1, len(self.array)):
            result = min(result, self.array[i]-self.array[i-1])
    
        return result