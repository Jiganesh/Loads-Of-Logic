from collections import deque

class Solution:
    def isBipartite(self, graph) -> bool:
        
    
        visited = [-1]* len(graph)
        
        g = {}
        
        for node, children  in enumerate(graph):
            g[node]=children
            
        
        
        def bipartite_or_not(root):
            q = deque()
            q.append((root,1))
            
            while q:
                node, bit = q.popleft()
                if visited[node] == -1:
                    visited[node]=bit
                    for child in g[node]:
                        q.append((child, bit^1))
                elif bit != visited[node]:
                    return False
                
            return True
        
        for i in range (len(graph)):
            if visited[i]==-1:
                if bipartite_or_not(i) == False:
                    return False
        return True
    
graph =  [[1,2,3],[0,2],[0,1,3],[0,2]]
# index 0 will be node 0 with edges 1,2,3
# index 1 will be node 1 with edges 0,2