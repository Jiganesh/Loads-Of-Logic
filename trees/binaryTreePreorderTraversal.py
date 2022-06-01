# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    # Runtime: 23 ms, faster than 53.84% of Python online submissions for Binary Tree Preorder Traversal.
    # Memory Usage: 13.4 MB, less than 77.67% of Python online submissions for Binary Tree Preorder Traversal.
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.array = []        
        def helper(root):
            if root:
                self.array.append(root.val)
                helper(root.left)
                helper(root.right)
                
        helper(root)
        return self.array
    
    
    # Runtime: 44 ms, faster than 5.30% of Python online submissions for Binary Tree Preorder Traversal.
    # Memory Usage: 13.4 MB, less than 51.07% of Python online submissions for Binary Tree Preorder Traversal.
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack= []
        result = []
        stack.append(root)
        
        while stack:
            val = stack.pop()
            if val : 
                result.append(val.val)
                if val.right:stack.append(val.right)
                if val.left :stack.append(val.left)

        return result
    
    
        
        
        
        