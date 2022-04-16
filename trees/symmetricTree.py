# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Runtime: 45 ms, faster than 59.42% of Python3 online submissions for Symmetric Tree.
    # Memory Usage: 13.9 MB, less than 95.27% of Python3 online submissions for Symmetric Tree.
    
    def isSymmetric(self, root):
    
        def helper(p, q):
            
            if p ==None and q==None:
                return True
            elif p ==None or q==None:
                return False
            elif p.val != q.val:
                return False
            else:
                return helper(p.left, q.right) and helper(p.right, q.left)
            
        return helper(root.left, root.right)