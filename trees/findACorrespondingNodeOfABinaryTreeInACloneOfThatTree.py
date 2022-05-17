# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # Runtime: 1016 ms, faster than 21.69% of Python online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
    # Memory Usage: 30.7 MB, less than 6.02% of Python online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
    
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        
                
        
        def helper(original , cloned, target):
            
            if (original==target): return cloned

            if original and cloned:
                return helper(original.left, cloned.left,target) or helper(original.right, cloned.right,target)
            
            return None
            
                
        TreeNodeClone = helper(original, cloned, target)
        return TreeNodeClone
        
        
        