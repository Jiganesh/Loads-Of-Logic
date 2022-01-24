# https://leetcode.com/problems/remove-covered-intervals/

class Solution:    
    
    # Submitted by @Jiganesh
    
    # Runtime: 68 ms, faster than 98.46% of Python online submissions for Remove Covered Intervals.
    # Memory Usage: 14.1 MB, less than 15.38% of Python online submissions for Remove Covered Intervals.


    # TC : O(NLogN)
    # SC : O(1)
    
    # literally merge interval and keep track
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x: x[0])
        
        c= intervals[0][0]
        d = intervals[0][1]
        count = len(intervals)
        
        for i in range ( 1, len(intervals)):
            a = intervals [i][0]
            b = intervals [i][1]
            
            if (c<=a and b<=d ) or (a<=c and d<=b):
                count-=1
                d = max(b,d)
            else:
                c= intervals[i][0]
                d = intervals[i][1]
        return count
    
    # TC : O(NLogN)
    # SC : O(1)
    # Smart , Intuative and Aesthetic solution
    
    # If merge possible - reduce that block 
    
    def removeCoveredIntervalsApproach2(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort(key = lambda x: (x[0],-x[1]))
        count = len(intervals)
        
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= prev: count-=1
            else : prev = intervals [i][1]
                
        return count;
    