# https://leetcode.com/problems/maximum-binary-tree-ii/

# https://leetcode.com/problems/maximum-binary-tree-ii/discuss/243214/Detailed-Explanation-With-Proof-Of-Correctness

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Runtime: 67 ms, faster than 18.72% of Python3 online submissions for Maximum Binary Tree II.
    # Memory Usage: 13.9 MB, less than 45.11% of Python3 online submissions for Maximum Binary Tree II.
    
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        parent_node, current_node = None, root
        
        while current_node and current_node.val > val:
            parent_node , current_node = current_node, current_node.right
            
        new_node = TreeNode(val)
        new_node.left = current_node
        
        if parent_node : parent_node.right = new_node
        
        return root if root.val > val else new_node
    
    
    
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