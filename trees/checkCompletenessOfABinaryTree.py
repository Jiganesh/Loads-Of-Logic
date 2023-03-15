# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root])

        null_node_found = False
        while queue:

            node = queue.popleft()
            if node == None:
                null_node_found = True
            else:
                if null_node_found == True:
                    return False
                else:
                    queue.append(node.left)
                    queue.append(node.right)
        return True
