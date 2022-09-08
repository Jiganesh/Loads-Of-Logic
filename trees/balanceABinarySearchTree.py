# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Runtime: 1067 ms, faster than 8.25% of Python3 online submissions for Balance a Binary Search Tree.
    # Memory Usage: 21.6 MB, less than 20.53% of Python3 online submissions for Balance a Binary Search Tree.
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        array =[]
        def helper(root):
            
            if root:
                helper(root.left)
                array.append(root.val)
                helper(root.right)
                
        helper(root)
        
        
        def construct_tree(array):
            
            if not array : return None
            
            mid = len(array)//2
            root = TreeNode(array[mid])
            
            root.left = construct_tree(array[:mid])
            root.right = construct_tree(array[mid+1:])
            
            return root
        
        return construct_tree(array)