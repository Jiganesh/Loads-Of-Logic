# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution(object):
    
    # Runtime: 5195 ms, faster than 16.74% of Python online submissions for Maximum Length of Repeated Subarray.
    # Memory Usage: 34.7 MB, less than 67.66% of Python online submissions for Maximum Length of Repeated Subarray.
    
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        dp = [ [0]* (len(nums1)+1) for i in range (len(nums2)+1)]
        
        
        maximum = float('-inf')
        
        for i in range (1, len(nums2)+1):
            for j in range (1, len(nums1)+1):
         
                if nums2[i-1] == nums1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else :
                    dp[i][j] = 0
                                        
                maximum = max(dp[i][j], maximum)        
        return maximum
    