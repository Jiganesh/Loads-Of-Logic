# https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        red_nodes = defaultdict(list)
        blue_nodes = defaultdict(list)

        BLUE = "BLUE"
        RED = "RED"

        for u, v in redEdges:
            red_nodes[u].append(v)

        for u, v in blueEdges:
            blue_nodes[u].append(v)

        
        # Implement BFS

        result = [-1 for i in range(n)]
        result[0] = 0

        q = deque([])
        q.append([0, 0, None]) # node, length, color

        visited = set()
        visited.add((0, None))

        while q:
            node, length, color = q.popleft()
            if result[node]==-1:
                result[node] = length
            
            if color != BLUE:
                for children in red_nodes[node]:
                    if (children, BLUE) not in visited:
                        visited.add((children, BLUE))
                        q.append([children, length+1, BLUE])
            
            if color != RED:
                for children in blue_nodes[node]:
                    if (children, RED) not in visited:
                        visited.add((children, RED))
                        q.append([children,length+1, RED])

        return result
