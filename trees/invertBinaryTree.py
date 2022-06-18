# https://leetcode.com/problems/invert-binary-tree/



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Runtime: 24 ms, faster than 99.28% of Python3 online submissions for Invert Binary Tree.
    # Memory Usage: 13.8 MB, less than 95.80% of Python3 online submissions for Invert Binary Tree.
    
    def invertTree(self, root) :
        
        def helper(root):
            if root:
                root.left, root.right = root.right, root.left
                helper(root.left)
                helper(root.right)
                
        helper(root)
        return root
    
    # Iterative Approach
    
    def invertTree(self, root):
        stack = [root]
        # each node must swap its children
        # swap pairs from top to bottom until dfs ends
        while stack:
            node = stack.pop()
            # children may be null, swap anyway
            if node:
                node.right, node.left = node.left, node.right
                stack.extend([node.right, node.left])
        return root