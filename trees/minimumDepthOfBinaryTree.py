# https://www.youtube.com/watch?v=JrrPcXix8zo




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    # Runtime: 1193 ms, faster than 25.94% of Python online submissions for Minimum Depth of Binary Tree.
    # Memory Usage: 96.3 MB, less than 16.34% of Python online submissions for Minimum Depth of Binary Tree.
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(root):
            
            if root == None:
                return 0
            
            else:
                
                minLeft = helper(root.left)
                minRight = helper(root.right)
                
                if minLeft ==0 or minRight ==0:
                    return 1+max(minLeft, minRight)
                
                return 1+ min(minLeft, minRight)
            
        return helper(root)