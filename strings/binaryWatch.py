
class Solution(object):
    
    # Runtime: 29 ms, faster than 40.48% of Python online submissions for Binary Watch.
    # Memory Usage: 13.5 MB, less than 38.10% of Python online submissions for Binary Watch.
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        
        result = []
        
        for i in range (0,12):
            for j in range (0,60):
                if bin(i).count("1")+bin(j).count("1")== turnedOn:
                    minutes = "0"+str(j) if j  <10  else str(j)
                    hours = str(i)
                    result.append(":".join([hours, minutes]))
                    
        return result