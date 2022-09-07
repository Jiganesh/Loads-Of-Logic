# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    # Runtime: 35 ms, faster than 94.55% of Python online submissions for Construct String from Binary Tree.
    # Memory Usage: 16.9 MB, less than 10.00% of Python online submissions for Construct String from Binary Tree.
    
    # Time complexity : O(n) The preorder traversal is done over the nnn nodes of the given Binary Tree.
    # Space complexity : O(n) The depth of the recursion tree can go upto nnn in case of a skewed tree.

    
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def helper ( root ):
            
            
            if not root:
                return ""
            
            left = ""
            right = ""
            
            if root.left :
                left = "(" + str(helper(root.left))+ ")"
                
            if root.right :
                left = "()"  if left == "" else left
                right = "("+ str(helper(root.right)) +")"
                
            return str(root.val)+left+right
        
        return helper(root)
            
        
        
                