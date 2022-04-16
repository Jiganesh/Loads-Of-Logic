# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        
class Solution:
    
    
    # Runtime: 30 ms, faster than 89.61% of Python3 online submissions for Same Tree.
    # Memory Usage: 13.9 MB, less than 78.67% of Python3 online submissions for Same Tree.
    
    def isSameTree(self, p, q) -> bool:
    
        def helper(p, q):
            
            if p  or q:
                
                if not p or not q or (q and p.val != q.val):
                    return False
                else :
                    return helper(p.left, q.left) and helper(p.right , q.right)
                    
            return True
                    
            
        return helper(p,q)
    
    
    # Aesthetic and Memory Efficient solution
    
    def isSameTree(self, p, q) -> bool:

        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False