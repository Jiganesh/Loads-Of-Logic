# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        q = [root]
        heap = []

        while q:
            level_sum = sum([i.val for i in q])
            heapq.heappush(heap, -level_sum)
            q = [child for p in q for child in [p.left, p.right] if child]

        result = -1
        while k :
            result = -heapq.heappop(heap) if heap else -1
            k-=1

        return result