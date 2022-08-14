# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # Runtime: 131 ms, faster than 42.21% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    # Memory Usage: 18.8 MB, less than 68.62% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root, p, q):
            
            if root:
                
                if p.val <root.val and q.val < root.val:
                    return helper(root.left,p, q)
                elif p.val >root.val and q.val >root.val:
                    return helper(root.right,p,q )
                else:
                    return root
                
        return helper(root, p, q)
        