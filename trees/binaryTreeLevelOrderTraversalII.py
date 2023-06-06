# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = deque([root])
        result_q = deque([])

        while q:

            result_q.appendleft([i.val for i in q if i])
            q = [child for p in q for child in [p.left, p.right] if child]

        return result_q

