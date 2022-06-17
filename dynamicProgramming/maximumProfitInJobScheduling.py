# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

from functools import lru_cache
import heapq


class Solution:
    
    # TC : O(N log N)
    # SC : O(N)
    def jobScheduling(self, startTime, endTime , profit):
        
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        
        heap = []
        max_profit = 0
        max_profit_before_start = 0 
        
        for start, end , profit_in_time in jobs:
            
            while heap and heap[0][0] <= start:
                _ , profit_till_now = heapq.heappop(heap)
                max_profit_before_start = max(max_profit_before_start, profit_till_now)
                
            heapq.heappush(heap, (end, profit_in_time+ max_profit_before_start))
            max_profit = max(max_profit, profit_in_time+max_profit_before_start)
            
        return max_profit

    # Recursion 
    # TC : (2^N)
    # SC : O(N)
                    
    def jobScheduling(self, startTime, endTime , profit):

        def helper(index, end, profit_till_now):
            
            if index==len(profit):
                return profit_till_now
            
            start_interval , end_interval, profit_in_interval = jobs[index]
            if end <= start_interval:
                return max(helper(index+1, end_interval, profit_till_now+profit_in_interval), helper(index+1, end, profit_till_now))
            else:
                return helper(index+1, end, profit_till_now)
                
            
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        
        return helper(0,0, 0)
            
    def jobScheduling(self, startTime, endTime , profit):
    
        @lru_cache(None)
        def helper(index):
            if index >= N:
                return 0
            
            j = index+1
            while j < N and jobs[j][0]<jobs[index][1]: 
                j+=1
            
            inc = jobs[index][2]+ helper(j)
            exc = helper(index+1)
            
            return max(inc, exc)
                      
            
        jobs = list(zip(startTime, endTime, profit))
        N = len(jobs)
        jobs.sort()
        
        return helper(0)

                
                
        
    
            
            
    
            
    