# https://leetcode.com/problems/maximum-binary-tree-ii/

# https://leetcode.com/problems/maximum-binary-tree-ii/discuss/243214/Detailed-Explanation-With-Proof-Of-Correctness

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def helper(root, value):
            
            valNode = TreeNode(value)
            
            if not root:
                return valNode
            
            if root.val < value:
                valNode.left = root
                return valNode
            else:
                root.right = helper(root.right, value)
                return root
                
            
        return helper(root, val)