# https://leetcode.com/problems/delete-leaves-with-a-given-value/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def helper(root):

            if root:
                if root.left : 
                    root.left  = helper(root.left)
                if root.right: 
                    root.right = helper(root.right)

                if root.left == None and root.right == None and root.val == target:
                    root = None
                return root

        helper(root)
        if root and root.left == None and root.right == None and root.val == target:
            return None
        else : 
            return root