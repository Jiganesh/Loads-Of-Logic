# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    # Runtime: 19 ms, faster than 85.60% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
    # Memory Usage: 13.8 MB, less than 40.38% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root ==None : return []
        
        result = []
        queue = [root]
        
        while queue :
            result.append([i.val for i in queue])
            queue = [child for p in queue for child in [p.left, p.right] if child]
            
        return [result[i] if i%2==0 else result[i][::-1] for i in range(len(result))]
            
        
    