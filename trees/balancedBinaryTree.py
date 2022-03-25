# https://leetcode.com/problems/balanced-binary-tree/

from treeNode import TreeNode


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
