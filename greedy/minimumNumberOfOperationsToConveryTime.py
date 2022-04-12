# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    
    # Runtime: 45 ms, faster than 51.75% of Python3 online submissions for Minimum Number of Operations to Convert Time.
    # Memory Usage: 14 MB, less than 29.22% of Python3 online submissions for Minimum Number of Operations to Convert Time.
    
    def convertTime(self, current: str, correct: str) -> int:
        time1 = list(map(int, current.split(":")))
        totalTime1 = time1[0]*60+time1[1]
        
        
        time2= list(map(int, correct.split(":")))
        totalTime2 = time2[0]*60+time2[1]
        
        
        wanted = totalTime2 -totalTime1
        
        count = 0
        
        for i in [60, 15, 5, 1]:
            count += wanted//i
            wanted%=i
            
        return count
    
    
# Question : This is similar to coin change but that requires dp and not greedy. why does greedy work here?
# Answer : Let us make amount 6 with denominations [1,3,4]

# what greedy will do is return you 4 1 1 (number of coins 3)
# what dp will do is return 3 3 (number of coins 2)

# That is why in problems like coin change, we cannot use greedy algorithm because
# greedy makes choice optimal at moment 
# dp makes choice optimal considering all possiblities.
            
            
            