



class Solution(object):
    
    # Runtime: 1871 ms, faster than 31.47% of Python online submissions for Non-overlapping Intervals.
    # Memory Usage: 58.1 MB, less than 93.98% of Python online submissions for Non-overlapping Intervals.
    
    # TC : O(NLogN)
    # SC : O(1)
    def eraseOverlapIntervals(self, intervals):
        
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort(key=lambda x: (x[1], x[0]))
        
        prev = intervals[0][1]
        count=0
        for i in range (1, len(intervals)):
            if intervals[i][0]<prev:
                count+=1
            else :
                prev= intervals[i][1]
        return count
    

        