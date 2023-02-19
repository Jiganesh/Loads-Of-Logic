# https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)
        result = []

        def cut (root):
            if root.left:
                result.append(root.left)
            if root.right:
                result.append(root.right)
                
        def helper(root):

            if root:
                helper(root.left)
                helper(root.right)
                if root.left and root.left.val in to_delete:
                    cut(root.left)
                    root.left = None

                if root.right and root.right.val in to_delete:
                    cut(root.right)
                    root.right = None

                
        
        dummyNode = TreeNode(-1, root, None)
        helper(dummyNode)

        if root.val in to_delete:
            return result
        else:
            return [root]+ result
