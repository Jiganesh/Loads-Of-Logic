# https://leetcode.com/problems/all-possible-full-binary-trees/

from typing import List, Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # TC : O(2^N)
    # SC : O(2^N)
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        def helper(n):
            
            if n==0:
                return []
            if n==1:
                return [TreeNode(0)]
            
            res= []
            
            for num_of_nodes_on_left in range (0, n-1):
                
                num_of_nodes_on_right = n- 1 - num_of_nodes_on_left
                
                leftTrees , rightTrees = helper(num_of_nodes_on_left), helper(num_of_nodes_on_right)
                
                for leftTree in leftTrees:
                    
                    for rightTree in rightTrees:
                        
                        res.append(TreeNode(0, leftTree, rightTree))    
            return res

        return helper(n)
                
    # Optimized
    
    # TC: O(2^N)
    # SC: O(N)     
    
    
    # Runtime: 191 ms, faster than 88.45% of Python3 online submissions for All Possible Full Binary Trees.
    # Memory Usage: 18.8 MB, less than 37.30% of Python3 online submissions for All Possible Full Binary Trees.           

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        dp = { 0: [], 1 : [TreeNode(0)]}
        
        def helper(n):
            
            if n in dp:
                return dp[n]
            
            res= []
            
            for num_of_nodes_on_left in range (0, n-1):
                num_of_nodes_on_right = n- 1 - num_of_nodes_on_left
                
                leftTrees , rightTrees = helper(num_of_nodes_on_left), helper(num_of_nodes_on_right)
                
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        
                        res.append(TreeNode(0, leftTree, rightTree)) 
            
            dp[n] = res
            return res

        return helper(n)