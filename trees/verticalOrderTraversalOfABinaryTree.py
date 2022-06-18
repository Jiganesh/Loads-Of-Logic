# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Runtime: 54 ms, faster than 37.38% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
    # Memory Usage: 14.2 MB, less than 25.87% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
    
    def verticalTraversal(self, root):
        
        dictionary = defaultdict(list)
        
        def helper(root, order=0, traversal=0):
            
            if root:
                helper(root.left, order-1, traversal +1)
                dictionary[order].append((root.val, traversal))
                helper(root.right, order+1, traversal+1)
                
        helper(root)
        least_level, highest_level = min(dictionary.keys()), max(dictionary.keys())
        
        result_with_values = [sorted(dictionary[i], key= lambda x : (x[1],x[0])) for i in range (least_level, highest_level+1)]
        return [[j[0] for j in i] for i in result_with_values]
        
                
        
    
        
            
            
        