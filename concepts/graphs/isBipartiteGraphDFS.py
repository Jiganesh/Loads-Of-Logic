class Solution:
    def isBipartite(self, graph) -> bool:

        visited = [-1]* len(graph)
        
        g = {}
        
        for node, children  in enumerate(graph):
            g[node]=children
        
        def bipartite_or_not(root, bit):
            
            visited[root]=bit
            for i in g[root]:
                if visited[i]==-1:
                    if not bipartite_or_not(i, bit^1):
                        return False
                elif visited[i]==bit:
                    return False
            return True
            

        for i in range (len(graph)):
            if visited[i]==-1:
                if not bipartite_or_not(i,1):
                    return False
                
        return True
    
     