# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Submitted by Jiganesh
    
    
    # TC: O(NlogN)
    # SC: O(1)
    
    # Runtime: 72 ms, faster than 97.15% of Python3 online submissions for Search in a Binary Search Tree.
    # Memory Usage: 16.4 MB, less than 96.41% of Python3 online submissions for Search in a Binary Search Tree.
    def searchBST(self, root, val: int) :
    
        while root:
            if root.val == val :
                return root
            elif val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
                
 
        