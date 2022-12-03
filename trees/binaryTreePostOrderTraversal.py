# https://leetcode.com/problems/binary-tree-postorder-traversal/
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        stack = [root]


        while stack :
            node = stack[-1]
            
            if not node :
                stack.pop()
                continue

            if node.left:
                stack.append(node.left)
                node.left = None
            elif node.right:
                stack.append(node.right)
                node.right = None
            else:
                node = stack.pop()
                result.append(node.val)

        return result