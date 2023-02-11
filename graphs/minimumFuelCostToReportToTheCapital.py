# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], target: int) -> int:
        
        g = defaultdict(list)
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)
            
        result = []
            
        self.ans = 0 
        
        def helper(node, prev_node):
            count = 1
            for children in g[node]:
                if children != prev_node:
                    count += helper(children, node)

            if node != 0:
                self.ans += math.ceil(count/target)

            return count

        helper(0, -1)
        return self.ans
