# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    # Runtime: 34 ms, faster than 34.00% of Python online submissions for Binary Tree Level Order Traversal.
    # Memory Usage: 13.6 MB, less than 83.16% of Python online submissions for Binary Tree Level Order Traversal.
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None: return []
        
        result = []
        queue = [root]
        
        while queue:
            result.append([i.val for i in queue if i])
            queue = [child for p in queue for child in [p.left, p.right] if child]
            
        return result
        