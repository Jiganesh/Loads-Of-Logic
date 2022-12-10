# https://leetcode.com/problems/leaf-similar-trees/

from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def helper(root, array):

            if root:

                if root.left :
                    helper(root.left, array)
                if root.right:
                    helper(root.right, array)
                if not root.left and not root.right:
                    array.append(root.val)
            return array


        leaf1 = helper(root1,[])
        leaf2 = helper(root2,[])

        print(leaf1, leaf2)
        return leaf1 == leaf2