from collections import deque

# TC : O(N+E)
# SC : O(N+E)+O(N)+O(N)


graph = {1: [(2, 4), (3, 5), (5, 8)], 2: [(1, 4), (4, 2), (3, 3)], 3: [(1, 5), (2, 3), (4, 4), (5, 1)], 5: [(1, 8), (3, 1)], 4: [(2, 2), (3, 4)]}
root=1

# Iterative DFS

def iterative_dfs(root):
    stack = []
    visited=[]
    stack.append(root)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for i , weight in reversed(graph[node]):
                stack.append(i)
    print(visited)
            
iterative_dfs(root)





# Recursive DFS
visited = []
def recursive_dfs(root):
    if root and root not in visited:
        visited.append(root)
        for i, weight in graph[root]:
            recursive_dfs(i)
recursive_dfs(root)
print(visited)

