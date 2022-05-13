# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):

    #   Runtime: 86 ms, faster than 22.38% of Python online submissions for Populating Next Right Pointers in Each Node.
    #   Memory Usage: 16.4 MB, less than 45.09% of Python online submissions for Populating Next Right Pointers in Each Node.

    def connect(self, root):
        dummy = root
        while root and root.left:
            leftNode = root.left
            while root:
                root.left.next = root.right
                root.right.next =  root.next and root.next.left   # same as root.next.left if root.next else None
                root = root.next
            root = leftNode
        return dummy
            
            
            
