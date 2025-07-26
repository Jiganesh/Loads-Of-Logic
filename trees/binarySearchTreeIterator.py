# Definition for a binary tree node.

# https://leetcode.com/problems/binary-search-tree-iterator/
# Solution : https://www.youtube.com/watch?v=D2jMcmxU4bs

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    
    # TC : O(1)
    # SC : O(H)
    
    # Runtime: 90 ms, faster than 60.71% of Python3 online submissions for Binary Search Tree Iterator.
    # Memory Usage: 20.4 MB, less than 35.61% of Python3 online submissions for Binary Search Tree Iterator.

    def __init__(self, root):
        
        self.stack = []
        self.pushAllNodes(root)

    def next(self) -> int:
        
        current = self.stack.pop()
        self.pushAllNodes(current.right)
        return current.val     
        
    def pushAllNodes(self, node) -> None:
        
        while node :
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return bool(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()