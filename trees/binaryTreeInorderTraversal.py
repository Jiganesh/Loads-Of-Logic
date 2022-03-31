# https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # APPROACH 1
    # Runtime: 36 ms, faster than 73.28% of Python3 online submissions for Binary Tree Inorder Traversal.
    # Memory Usage: 13.8 MB, less than 63.72% of Python3 online submissions for Binary Tree Inorder Traversal.
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )

    # APPROACH 2
    # Runtime: 38 ms, faster than 66.97% of Python3 online submissions for Binary Tree Inorder Traversal.
    # Memory Usage: 13.9 MB, less than 63.72% of Python3 online submissions for Binary Tree Inorder Traversal.
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        def inorder_traversal(root: TreeNode, lst: list):
            if root is None:
                return
            inorder_traversal(root.left, lst)
            lst.append(root.val)
            inorder_traversal(root.right, lst)

        lst = []
        inorder_traversal(root, lst)
        return lst
