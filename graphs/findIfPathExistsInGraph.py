# https://leetcode.com/problems/find-if-path-exists-in-graph/
from typing import List
from collections import defaultdict, deque

class Solution:

    # Runtime: 2715 ms, faster than 65.04% of Python3 online submissions for Find if Path Exists in Graph.
    # Memory Usage: 300.9 MB, less than 24.84% of Python3 online submissions for Find if Path Exists in Graph.

    # DFS APPROACH
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def helper(node, destination):

            # Edge Case if source is destination
            if node == destination:
                return True

            if visited[node]==False:
                visited[node]=True
                for child in graph[node]:
                        if helper(child, destination): return True
            return False

        visited = [False]*n
        graph = defaultdict(list)

        for u, v  in edges:
            graph[u].append(v)
            graph[v].append(u)

        return helper(source, destination)

    # BFS APPROACH
    # Runtime: 2259 ms, faster than 84.02% of Python3 online submissions for Find if Path Exists in Graph.
    # Memory Usage: 104.9 MB, less than 76.51% of Python3 online submissions for Find if Path Exists in Graph.
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def helper(node, destination):

            queue = deque([node])
            while queue:
                node = queue.popleft()
                if node == destination:
                    return True

                for child in graph[node]:
                    if visited[child]==False:
                        visited[child]=True
                        queue.append(child)

            return False

        visited = [False]*n
        graph = defaultdict(list)

        for u, v  in edges:
            graph[u].append(v)
            graph[v].append(u)

        return helper(source, destination)


