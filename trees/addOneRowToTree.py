
# https://leetcode.com/problems/add-one-row-to-tree/

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        dummyNode = TreeNode(-1, root)
        q = [dummyNode]

        while q :

            depth-=1
            if depth==0:
                for child in q:
                    
                    child.left = TreeNode(val, child.left, None)
                    child.right = TreeNode(val, None, child.right)

            q = [child for p in q for child in (p.left, p.right) if child]
        return dummyNode.left