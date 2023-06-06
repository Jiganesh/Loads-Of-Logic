# https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], inform: List[int]) -> int:
        
        graph = defaultdict(list)

        for ind, mang in enumerate(manager):
            graph[mang].append(ind)
        
        def helper(root):
            
            ans = 0

            if inform[root] == 0:
                return 0

            for emp in graph[root]:
                val = helper(emp)
                ans = max(ans, val)
                
            return ans + inform[root]

        val = helper(headID)
        return val