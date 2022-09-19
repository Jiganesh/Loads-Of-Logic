# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Runtime: 88 ms, faster than 82.17% of Python3 online submissions for Count Complete Tree Nodes.
    # Memory Usage: 21.5 MB, less than 13.42% of Python3 online submissions for Count Complete Tree Nodes.
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    # Runtime: 72 ms, faster than 98.00% of Python3 online submissions for Count Complete Tree Nodes.
    # Memory Usage: 21.4 MB, less than 87.36% of Python3 online submissions for Count Complete Tree Nodes.

    def countNodes(self, root: TreeNode) -> int:
        
        def helper(root):
            
            depth_left = depth_right = 0
            left_node = right_node = root
            
            while left_node or right_node:
                if left_node :
                    left_node = left_node.left
                    depth_left+=1
                if right_node :
                    right_node = right_node.right
                    depth_right+=1
                    
            if depth_left == depth_right:
                return 2 ** depth_left - 1
            else:
                return 1+ helper(root.left)+ helper(root.right)
            
        return helper(root)
