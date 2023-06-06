# https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        lookup = defaultdict(int)
        
        def sum_at_level(root, height):
            
            if root:
                left_val = root.left.val if root.left else 0
                right_val = root.right.val if root.right else 0

                lookup[height] +=  left_val+right_val

                sum_at_level(root.left, height+1)
                sum_at_level(root.right, height+1) 
            
            return 0
        
        lookup[0] = root.val
        sum_at_level(root, 1)
        
        
        def dfs (root, height):
            
            if root:
                
                left_val = root.left.val if root.left else 0
                right_val = root.right.val if root.right else 0
                
                
                sum_at_node = left_val + right_val
                if root.left:
                    root.left.val = lookup[height]-sum_at_node
                if root.right:
                    root.right.val = lookup[height]-sum_at_node

                dfs( root.left, height+1)
                dfs( root.right, height+1) 
                
            return 0
        
        dfs(root, 1)
        root.val = 0

        return root
                