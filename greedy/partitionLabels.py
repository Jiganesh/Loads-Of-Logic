
class Solution(object):

    # TC : O(N)
    # SC : O(N) As there can be no more than 26 Letters 
    
    # Runtime: 44 ms, faster than 38.81% of Python online submissions for Partition Labels.
    # Memory Usage: 13.6 MB, less than 12.27% of Python online submissions for Partition Labels.
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        dictionary = {i : [float('inf'), float('-inf')] for i in s}
        for i in range(len(s)):
            
            dictionary[s[i]][0]= min(dictionary[s[i]][0], i)
            dictionary[s[i]][1]= max(dictionary[s[i]][1], i)
            
        intervals = [i for  i in dictionary.values()]        
        intervals.sort()
        

        start  = intervals[0][0]
        end = intervals[0][1]
        result = []
        
        for i in range(0, len(intervals)):
            interval = intervals[i]
            
            if end >= interval[0]:
                end = max(end, interval[1])
            else :
                result.append(end-start+1) # As we want length of String
                
                start = interval[0]
                end = interval[1]
                
        result.append (len(s)- sum(result))  
        return result