# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    # Runtime: 51 ms, faster than 79.48% of Python3 online submissions for Maximum Width of Binary Tree.
    # Memory Usage: 14.8 MB, less than 46.11% of Python3 online submissions for Maximum Width of Binary Tree.
    def widthOfBinaryTree(self, root) :
        
        q = [(1, root)]
        max_len = 1
        
        while q:
            
            max_len = max(max_len, q[-1][0]-q[0][0]+1) 
            q = [child for number , p in q  for child in enumerate((p.left, p.right), 2*number) if child[1]]
            
        return max_len