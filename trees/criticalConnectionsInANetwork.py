# https://leetcode.com/problems/critical-connections-in-a-network/

class Solution:
    
    # Runtime: 2172 ms, faster than 98.00% of Python3 online submissions for Critical Connections in a Network.
    # Memory Usage: 65.7 MB, less than 98.95% of Python3 online submissions for Critical Connections in a Network.    
    
    def criticalConnections(self, n: int, connections) :
        
        
        graph = [[] for _ in range(n)] ## vertex i ==> [its neighbors]
		
        currentRank = 0 ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level
		
        lowestRank = [i for i in range(n)] ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i
		
        visited = [False for _ in range(n)] ## common DFS/BFS method to mark whether this node is seen before
        
        ## build graph:
        for connection in connections:
            ## this step is straightforward, build graph as you would normally do
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        
        res = []
        prevVertex = -1 ## This -1 a dummy. Does not really matter in the beginning. 
		## It will be used in the following DFS because we need to know where the current DFS level comes from. 
		## You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.
		
        currentVertex = 0 ## we start the DFS from vertex num 0 (its rank is also 0 of course)
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        return res
    
    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):

        visited[currentVertex] = True 
        lowestRank[currentVertex] = currentRank

        for nextVertex in graph[currentVertex]:
            if nextVertex == prevVertex:
                continue ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

            if not visited[nextVertex]:
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
				# We avoid visiting visited nodes here instead of doing it at the beginning of DFS - 
				# the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.

            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex]) 
			# take the min of the current vertex's and next vertex's ranking
            if lowestRank[nextVertex] >= currentRank + 1: ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
                res.append([currentVertex, nextVertex])
        