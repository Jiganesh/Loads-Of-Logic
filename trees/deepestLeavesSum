# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root) -> int:
        
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
            print([i.val for i in q])
        return sum(node.val for node in pre)
    
    
    
        #[child for p in q for child in [p.left, p.right] if child]
        
        # Above line translates too
        
        # current = []
        # for p in q:
        #     for child in [p.left, p.right] :
        #         if child:
        #             current.append(child)
        # q = current
    
    