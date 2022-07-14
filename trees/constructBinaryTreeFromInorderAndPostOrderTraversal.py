# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    # Runtime: 277 ms, faster than 24.75% of Python online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    # Memory Usage: 52.9 MB, less than 49.09% of Python online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
 
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(inorder):
            
            root =None
            if inorder:
                root_val = postorder.pop()
                root_ind = inorder.index(root_val)
                
                root = TreeNode(root_val)
                root.right = helper(inorder[root_ind+1:])
                root.left = helper(inorder[:root_ind])
                
            return root
        
        return helper(inorder)
    
    
    # Runtime: 76 ms, faster than 77.89% of Python online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    # Memory Usage: 19 MB, less than 65.52% of Python online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

    # Most Optimal because of Pointers
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        
        ind = {val : ind for ind, val in enumerate(inorder)}
        def helper(instart, inend ,poststart, postend):
        
            if instart>inend or poststart>postend: return None

            root_val = postorder[postend]
            root_ind = ind[root_val]
        
            root  = TreeNode(root_val)
            element_to_right =inend - root_ind
        
            root.right = helper(root_ind+1, inend, postend-element_to_right, postend-1)
            root.left = helper(instart, root_ind-1, poststart, postend-element_to_right-1)
            
            return root
    
        return helper(0, len(inorder)-1, 0, len(postorder)-1)
                
                