# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root ==None:
            return TreeNode(val)
        
        currentnode = root
        while(currentnode):
            if currentnode.val < val :
                if currentnode.right != None:
                    currentnode = currentnode.right
                else:
                    currentnode.right= TreeNode(val)
                    break;
            else:
                if currentnode.left != None:
                    currentnode = currentnode.left
                else:
                    currentnode.left = TreeNode(val)
                    break;
        return root