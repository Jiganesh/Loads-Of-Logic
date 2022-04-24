import sys

# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree TreeNode.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Runtime: 40 ms, faster than 97.41% of Python3 online submissions for Validate Binary Search Tree.
    # Memory Usage: 16.5 MB, less than 46.51% of Python3 online submissions for Validate Binary Search Tree.
    def isValidBST(self, root: TreeNode) -> bool:
        def __is_bst(root: TreeNode, min, max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False
            return __is_bst(root.left, min, root.val) and __is_bst(
                root.right, root.val, max
            )

        return __is_bst(root, -sys.maxsize, sys.maxsize)
