import bisect, heapq, operator, math
from typing import List
from itertools import accumulate
from collections import defaultdict, Counter, deque
from functools import lru_cache, cmp_to_key



graph = {1: [(2, 4), (3, 5), (5, 8)], 2: [(1, 4), (4, 2), (3, 3)], 3: [(1, 5), (2, 3), (4, 4), (5, 1)], 5: [(1, 8), (3, 1)], 4: [(2, 2), (3, 4)]}
root=1

visited = []
def dfs_recursive (root):
    
    if root not in visited:
        visited.append(root)
        for child ,weight in graph[root]:
            if child not in visited:
                dfs_recursive(child)
       
def dfs_iterative(root):
    stack = [root]
    visited= []     

    
    while stack :
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for child ,weight in reversed(graph[node]):
                if child not in visited:
                    stack.append(child)
                    
    print(visited)
                
    

dfs_recursive(root)
print(visited)
dfs_iterative(root)
        