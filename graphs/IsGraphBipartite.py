# https://leetcode.com/problems/is-graph-bipartite/

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
    
testCase = [
    [[1,2,3],[0,2],[0,1,3],[0,2]],
    [[1,3],[0,2],[1,3],[0,2]],
    [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
]     

for i in testCase:
    print(Solution().isBipartite(i))
     
