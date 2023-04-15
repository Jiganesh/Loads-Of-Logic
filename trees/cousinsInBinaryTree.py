# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        x_data = [-1 , -1]
        y_data = [-1, -1]
        def helper(root, height, parent):
            if root:

                if root.val == x:
                    x_data[0], x_data[1] = parent, height
                if root.val == y:
                    y_data[0], y_data[1]  = [parent, height]

                helper(root.left, height+1, root)
                helper(root.right, height+1, root)

        helper(root, 0, -1)
        # data = [parent, height]
        return x_data[0] != y_data[0] and x_data[1] == y_data[1]

                





                