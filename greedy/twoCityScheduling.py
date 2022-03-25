# https://leetcode.com/problems/two-city-scheduling/

class Solution(object):
    
    # Submitted by Jiganesh 
    
    # Runtime : 32 ms
    
    def twoCitySchedCost(self, costs):
        """
        
        :type costs: List[List[int]]
        :rtype: int
        """
        
        costs.sort(key = lambda x: x[0]-x[1])
        mid = len(costs)//2
        return sum ([i[0] for i in costs[:mid]])+ sum(i[1] for i in costs[mid:])
        
    # Runtime: 19 ms, faster than 97.02% of Python online submissions for Two City Scheduling.
    # Memory Usage: 13.3 MB, less than 82.14% of Python online submissions for Two City Scheduling.
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        costs.sort(key = lambda x: x[0]-x[1])
        minimumCost =0
        mid = len(costs)//2
        
        for i in range (len(costs)): 
            minimumCost+=costs[i][0] if i< mid else costs[i][1]
            
        return minimumCost
        