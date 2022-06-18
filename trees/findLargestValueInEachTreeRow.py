# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # Runtime: 84 ms, faster than 26.08% of Python3 online submissions for Find Largest Value in Each Tree Row.
    # Memory Usage: 16.2 MB, less than 69.94% of Python3 online submissions for Find Largest Value in Each Tree Row.
    def largestValues(self, root) :
        
        if not root : return []
        
        result = []
        q = [root]
        while q:
            result.append(max([i.val for i in q ]))
            q = [child for p in q for child in [p.left, p.right] if child]
            
        return result