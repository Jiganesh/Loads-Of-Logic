# https://leetcode.com/problems/maximum-earnings-from-taxi/


# SIMILAR PROBLEM : MAXIMUM PROFIT IN JOB SCHEDULING
import heapq

class Solution:
    
    # Runtime: 3941 ms, faster than 5.82% of Python3 online submissions for Maximum Earnings From Taxi.
    # Memory Usage: 33.8 MB, less than 62.71% of Python3 online submissions for Maximum Earnings From Taxi.
    def maxTaxiEarnings(self, n: int, rides) :
        
        for i in range(len(rides)):
            start, end , tip = rides[i]
            rides[i] = [start, end , end-start+tip]
            
        rides.sort()
        heap = []

        current = 0
        maximum = 0
        
        for ride in rides:
            start , end , profit  = ride
            while heap and heap[0][0]<=start:
                _, profit_made = heapq.heappop(heap)
                current = max(current, profit_made)
                
            
            total_profit = current + profit
            heapq.heappush(heap,(end, total_profit))
            maximum = max(maximum, total_profit)
        
        return maximum
                