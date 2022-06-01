# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    
    # Runtime: 55 ms, faster than 41.35% of Python online submissions for N-ary Tree Preorder Traversal.
    # Memory Usage: 16.3 MB, less than 73.08% of Python online submissions for N-ary Tree Preorder Traversal.
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                while node.children:
                    stack.append(node.children.pop())
        return result
    
    # Runtime: 65 ms, faster than 27.40% of Python online submissions for N-ary Tree Preorder Traversal.
    # Memory Usage: 16.6 MB, less than 14.66% of Python online submissions for N-ary Tree Preorder Traversal.
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        self.array = []
        
        def helper(root):
            if root:
                self.array.append(root.val)
                for node in root.children:
                    helper(node)
                    
        helper(root)
        return self.array
    
    
    
    
    