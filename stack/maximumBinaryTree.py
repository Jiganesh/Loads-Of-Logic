
# https://leetcode.com/problems/maximum-binary-tree/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # Runtime: 391 ms, faster than 26.38% of Python3 online submissions for Maximum Binary Tree.
    # Memory Usage: 14.3 MB, less than 99.12% of Python3 online submissions for Maximum Binary Tree.
    
    
    # TC : O(N^2)
    # SC : O(N)
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def helper(array):
            
            if not array:
                return None
            
            max_ind = 0
            for ind in range (len(array)):
                if array[ind]>array[max_ind]:
                
                    max_ind = ind
                
            root = TreeNode (array[max_ind])
            root.left = helper(array[:max_ind])
            root.right= helper(array[max_ind+1:])
            
            return root
        
        return helper(nums)


    # TC: O(N)
    # SC: O(N)

    # Runtime: 187 ms, faster than 98.88% of Python3 online submissions for Maximum Binary Tree.
    # Memory Usage: 14.6 MB, less than 20.31% of Python3 online submissions for Maximum Binary Tree.

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        stack_of_nodes = []
        
        for num in nums:
            
            node = TreeNode(num)
            last_node = None
            
            while stack_of_nodes and stack_of_nodes[-1].val < num:
                last_node = stack_of_nodes.pop()
                
            node.left = last_node
            
            if stack_of_nodes:
                node_greater_than_current_node = stack_of_nodes[-1] 
                node_greater_than_current_node.right = node
            
            stack_of_nodes.append(node)
            
        return stack_of_nodes[0]
      