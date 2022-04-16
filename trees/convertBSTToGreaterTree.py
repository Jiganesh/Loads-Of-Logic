# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Runtime: 82 ms, faster than 89.47% of Python3 online submissions for Convert BST to Greater Tree.
    # Memory Usage: 16.7 MB, less than 77.23% of Python3 online submissions for Convert BST to Greater Tree.
    
    def convertBST(self, root):
    
        
        def helper(root, array):
            
            if root:
                helper(root.right, array)
                root.val += array[0]
                array[0] = root.val
                helper(root.left, array)
                
            return root
                
        array =[0]
        return helper(root, array)
                