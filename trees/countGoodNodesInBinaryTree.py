# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Runtime: 240 ms, faster than 98.68% of Python3 online submissions for Count Good Nodes in Binary Tree.
    # Memory Usage: 32.5 MB, less than 46.26% of Python3 online submissions for Count Good Nodes in Binary Tree.

    def goodNodes(self, root: TreeNode) -> int:
        
        self.result = 0
        def helper(root, max_seen_so_far = root.val):
            
            if root:
                
                if root.val >= max_seen_so_far:
                    self.result += 1
                    max_seen_so_far = root.val
                    
                helper(root.left, max_seen_so_far)
                helper(root.right, max_seen_so_far)
        
        helper(root)
        return self.result            
                    
                