# https://leetcode.com/problems/teemo-attacking/

class Solution(object):
    
    
    # Submitted by @Jiganesh
    
    # TC : O(N)
    # SC : O(1)
    
    '''
    Runtime: 224 ms, faster than 52.38% of Python online submissions for Teemo Attacking.
    Memory Usage: 14.7 MB, less than 65.31% of Python online submissions for Teemo Attacking.
    '''
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        totalTime = 0
        n = len(timeSeries)
        
        for i in  range(n):
            if (i != n-1)  and (timeSeries[i]+duration-1>= timeSeries[i+1]):
                totalTime+=timeSeries[i+1]-timeSeries[i]
            else:
                totalTime += duration
                
        return totalTime

        '''
        Example
        
        timeSeries = [1,5,7,8]  duration = 4
        
        poisonEffect remains from [t , t+ duration-1] (inclusive)
        
        poisonEffect Duration
        [1-4]  poison effect = 4
        [5-8]  poison effect 5 to 8 but after attack of 7 it will reset so it will be [5-7] poison effect = 2
               (5,6) because on 7 there will be next attack and this will be added in next part
        [7-10] poison effect 7 to 10 but after attack of 8 it will reset so it will be [7-8] poison effect =1
               (7) because on 8 there will be next attack and this will be added in next part
        [8-11] last element in timeSeries so it will have full duration poison effect = 4
        
        Hence Answer will be 11
        
        '''