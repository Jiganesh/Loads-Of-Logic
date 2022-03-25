# Definition for a binary tree node.


class TreeNode:
    def __init__(self) -> None:
        pass

    def __init__(self, val):
        self.val = val
        self.left = self.right = None

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
