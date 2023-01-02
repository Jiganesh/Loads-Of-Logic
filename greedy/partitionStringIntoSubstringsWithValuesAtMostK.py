# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution(object):
    def minimumPartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        number = 0
        result =0
        
        for num in s:
            
            number = number * 10 + int(num)

            if number > k:
                number = int(num)
                result +=1
                
            if number > k:
                return -1

        return result+1