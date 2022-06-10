from collections import deque


# TC : O(N+E)
# SC : O(N+E)+O(N)+O(N)


graph = {1: [(2, 4), (3, 5), (5, 8)], 2: [(1, 4), (4, 2), (3, 3)], 3: [(1, 5), (2, 3), (4, 4), (5, 1)], 5: [(1, 8), (3, 1)], 4: [(2, 2), (3, 4)]}
root=1

# Iterative BFS
def iterative_bfs(root):
    visited = []
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)    
            for i, weight in graph[node]:
                q.append(i)
        
    print(visited)
    
   
# Recursive BFS
visited_recursive = [] 
queue = deque()
queue.append(root)
def recursive_bfs(queue):
    node = queue.popleft()
    if node not in visited_recursive:
        visited_recursive.append(node)
        for i, weight in graph[node]:
            queue.append(i)
            
    if queue:
        recursive_bfs(queue)
        
    
iterative_bfs(root)
recursive_bfs(queue)
print(visited_recursive)