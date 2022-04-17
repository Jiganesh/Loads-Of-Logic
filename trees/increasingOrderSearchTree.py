# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    
    # Runtime: 29 ms, faster than 91.75% of Python3 online submissions for Increasing Order Search Tree.
    # Memory Usage: 14 MB, less than 13.79% of Python3 online submissions for Increasing Order Search Tree.
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        
        def helper(root, array):
            
            if root:
                helper(root.left, array)
                array.append(root.val)
                helper(root.right, array)
                
            return array
        
        array = helper(root, [])
        
        pointerOnRoot = root = TreeNode(-1)
        
        for i in array:
            
            root.right= TreeNode(i)
            root = root.right
        

        return pointerOnRoot.right