# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:       
             
    # Runtime: 76 ms, faster than 86.88% of Python3 online submissions for Recover Binary Search Tree.
    # Memory Usage: 14.2 MB, less than 65.76% of Python3 online submissions for Recover Binary Search Tree.
                
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        
        """
        
        self.first = None
        self.second = None
        self.prev = None
        
        def traverse(root):
            
            if root:
                
                traverse(root.left)
                
                if self.prev :
                    if self.first==None  and self.prev.val > root.val:
                        
                        self.first = self.prev
                        self.second = root
                        
                    elif self.first and self.prev.val > root.val:
                        
                        self.second = root
                        
                self.prev = root
                traverse(root.right)
        
        traverse(root)
        self.first.val , self.second.val = self.second.val , self.first.val
        
        
        
        