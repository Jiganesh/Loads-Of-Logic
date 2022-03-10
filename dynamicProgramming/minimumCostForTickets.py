# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution(object):   
    
    # Submitted by Jiganesh
    
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 28 ms, faster than 91.37% of Python online submissions for Minimum Cost For Tickets.
    # Memory Usage: 13.3 MB, less than 96.17% of Python online submissions for Minimum Cost For Tickets.
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0 for i in range(days[-1]+1)]
     
        start = days[0]
        end = days[-1]+1
        
        pointerondays =0
        for i in range(start, end):
            
            if i==days[pointerondays]:
                
                day1 = dp[i-1]+costs[0] if i-1>=start else costs[0]
                day2 = dp[i-7]+costs[1] if i-7>=start else costs[1]
                day3 = dp[i-30]+costs[2] if i-30>= start else costs[2]
        
                dp[i]= min(day1, day2,day3) 
                pointerondays+=1
            else :
                dp[i]=dp[i-1]
            
        return dp[-1]