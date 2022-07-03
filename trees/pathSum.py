# https://leetcode.com/problems/path-sum/


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Runtime: 68 ms, faster than 43.43% of Python3 online submissions for Path Sum.
    # Memory Usage: 15 MB, less than 58.01% of Python3 online submissions for Path Sum.
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def helper(root, sum=0):
            
            
            if root:
                if not root.left and not root.right and root.val+sum == targetSum : return True
                else :return helper(root.left, sum+root.val) or helper(root.right, sum+root.val)
            
            return False
        
        return helper(root)
            
                
                
                