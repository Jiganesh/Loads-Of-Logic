# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Runtime: 88 ms, faster than 82.17% of Python3 online submissions for Count Complete Tree Nodes.
    # Memory Usage: 21.5 MB, less than 13.42% of Python3 online submissions for Count Complete Tree Nodes.
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    # Runtime: 72 ms, faster than 98.00% of Python3 online submissions for Count Complete Tree Nodes.
    # Memory Usage: 21.4 MB, less than 87.36% of Python3 online submissions for Count Complete Tree Nodes.
    def countNodes(self, root: TreeNode) -> int:
        left_height, right_height = 0, 0
        current_node = root
        while current_node is not None:
            left_height += 1
            current_node = current_node.left
        current_node = root
        while current_node is not None:
            right_height += 1
            current_node = current_node.right
        if left_height == right_height:
            return pow(2, left_height) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
