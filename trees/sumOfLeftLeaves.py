# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # TC : O(2N)
    # SC : O(1)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def turn_right_nodes_zero(root):
            if root:
                turn_right_nodes_zero(root.left) 
                if root.right:
                    root.right.val = 0
                
                turn_right_nodes_zero(root.right)


        def sum_of_leaf_node(root):

           
            if root and root.left == None and root.right == None:
                self.summation += root.val
            
            if root:
                sum_of_leaf_node(root.left)
                sum_of_leaf_node(root.right)
                

        self.summation = 0
        root.val = 0
        turn_right_nodes_zero(root)
        sum_of_leaf_node(root)

        return self.summation
        

    # TC : O(N)
    # SC : O(1)

    # Just use a flag variable
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def helper(root, is_left):
            if root:

                if root.left == None and root.right == None and is_left:
                    return root.val
                
                left = helper(root.left, True)
                right = helper(root.right, False)

                return left + right 
                
            return 0
        
        return helper(root, False)
        


