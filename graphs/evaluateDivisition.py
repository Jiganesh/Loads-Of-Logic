# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        N = len(values)
        

        def dfs(u, v, visited, value, res):

            if u == v:
                res.append(value)
                return res
            
           
            for child in graph[u]:
                if child not in visited and (u,child) in lookup:
                    visited.add(child)
                    dfs(child, v, visited, value * lookup[(u,child)], res)
                    visited.remove(child)

            return res

            

        result = []

        graph = defaultdict(list)
        lookup = {}

        for ind, eq in enumerate(equations):
            u, v = eq
            graph[u].append(v)
            lookup[(u,v)] = values[ind]

            graph[v].append(u)
            lookup[(v,u)] = 1/ values[ind]

            lookup[(u, u)] = 1.0000
            lookup[(v, v)] = 1.0000



        for query in queries:
            u, v = query
            a= None
            if u in graph:
                a = dfs(u,v,set([u]), 1, [])
            if a :
                result.append(a[-1])
            else:
                result.append(-1)

        return result




        


