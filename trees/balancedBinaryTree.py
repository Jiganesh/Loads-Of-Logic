# https://leetcode.com/problems/balanced-binary-tree/

from treeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Runtime: 51 ms, faster than 91.61% of Python3 online submissions for Balanced Binary Tree.
    # Memory Usage: 18.7 MB, less than 60.30% of Python3 online submissions for Balanced Binary Tree.

    def isBalanced(self, root: TreeNode) -> bool:
        def is_balanced_tree(self, root: TreeNode) -> int:
            if root is None:
                return 0
            left_height = is_balanced_tree(self, root.left)
            if left_height == -1:
                return -1
            right_height = is_balanced_tree(self, root.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1

        return not is_balanced_tree(self, root) == -1
