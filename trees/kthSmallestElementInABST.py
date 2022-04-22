# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Runtime: 48 ms, faster than 91.89% of Python3 online submissions for Kth Smallest Element in a BST.
    # Memory Usage: 18.2 MB, less than 13.38% of Python3 online submissions for Kth Smallest Element in a BST.
    def kthSmallest(self, root, k: int) -> int:
        self.k = k
        self.kthElement = -1

        def helper(root):
            if root:
                helper(root.left)
                self.k -= 1
                if self.k == 0:
                    self.kthElement = root.val
                    return self.kthElement
                helper(root.right)

        helper(root)
        return self.kthElement
