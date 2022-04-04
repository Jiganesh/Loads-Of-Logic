# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 36 ms, faster than 84.23% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 14.3 MB, less than 16.33% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        if root is None:
            return result
        stk1, stk2 = [], []
        stk1.append(root)
        while len(stk1) > 0 or len(stk2) > 0:
            list_1 = []
            while len(stk1) > 0:
                current_node = stk1.pop()
                list_1.append(current_node.val)
                if current_node.left is not None:
                    stk2.append(current_node.left)
                if current_node.right is not None:
                    stk2.append(current_node.right)
            if len(list_1) > 0:
                result.append(list_1)
            list_2 = []
            while len(stk2) > 0:
                current_node = stk2.pop()
                list_2.append(current_node.val)
                if current_node.right is not None:
                    stk1.append(current_node.right)
                if current_node.left is not None:
                    stk1.append(current_node.left)
            if len(list_2) > 0:
                result.append(list_2)
        return result
