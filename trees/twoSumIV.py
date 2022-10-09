# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        lookup = set()

        def helper(root):

            if root:

                if k-root.val in lookup:
                    return True
                else:
                    lookup.add(root.val)
                    return helper(root.left) or helper(root.right)

        return helper(root)
