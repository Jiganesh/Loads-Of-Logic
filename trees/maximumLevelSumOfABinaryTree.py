# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = [root]
        level, result_level = 1, -1
        result_summation = float("-inf")
        
        while q :
            summation = sum([i.val for i in q])

            if result_summation < summation :
                result_summation = summation
                result_level = level

            q = [child for p in q for child in [p.left, p.right] if child]
            level += 1
            
        return result_level

