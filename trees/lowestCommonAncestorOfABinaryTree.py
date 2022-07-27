# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Runtime: 82 ms, faster than 81.60% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    # Memory Usage: 26.2 MB, less than 61.82% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        if root == None or root == p or root == q:
            return root
        
		# Find p/q in left subtree
        l = self.lowestCommonAncestor(root.left, p, q)
		
		# Find p/q in right subtree
        r = self.lowestCommonAncestor(root.right, p, q)
        
		# If p and q found in left and right subtree of this node, then this node is LCA
        if l and r:
            return root
        
		# Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
        return l if l else r