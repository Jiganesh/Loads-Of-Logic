# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution(object):
    # Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Find the K-Beauty of a Number.
    # Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find the K-Beauty of a Number.
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        s = str(num)
        array = [ int(s[i:i+k]) for i in range (len(s)-k+1)]
        
        count = 0
        for i in array:
            if i>0 and num%i==0:
                count+=1
        return count