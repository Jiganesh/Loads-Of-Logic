from typing import List , Optional
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Runtime: 1357 ms, faster than 75.00% of Python3 online submissions for Amount of Time for Binary Tree to Be Infected.
    # Memory Usage: 157.3 MB, less than 50.00% of Python3 online submissions for Amount of Time for Binary Tree to Be Infected.
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = defaultdict(list)
        
        def helper(root):
            if root:
                if root.left:
                    graph[root.left.val].append(root.val)
                    graph[root.val].append(root.left.val)
                if root.right:
                    graph[root.right.val].append(root.val)
                    graph[root.val].append(root.right.val)
                    
                helper(root.left)
                helper(root.right)
                
        helper(root)
        not_visited = {i : True for i in graph}
        
        def bfs(start, minutes=0):
            
            queue = deque()
            queue.append((start, 0))
            max_minutes = 0
            while queue:

                node, minutes = queue.popleft()
                max_minutes = max(minutes, max_minutes)
                not_visited[node]=False
                
                for child in graph[node]:
                    if not_visited[child]:
                        queue.append((child, minutes+1))
                        
            return max_minutes
        
        return bfs(start)
