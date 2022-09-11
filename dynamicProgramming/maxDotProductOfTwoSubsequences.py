# https://leetcode.com/problems/max-dot-product-of-two-subsequences/

from typing import List

class Solution:

    # Runtime: 910 ms, faster than 40.39% of Python3 online submissions for Max Dot Product of Two Subsequences.
    # Memory Usage: 89.5 MB, less than 26.92% of Python3 online submissions for Max Dot Product of Two Subsequences.

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = {}
        
        def helper(i, j, nums1, nums2):
            

            if (i, j) in dp:
                return dp[(i, j)]
            
            if i< n1 and j<n2:
                
                #case1
                ans1 = nums1[i]*nums2[j] + helper(i+1, j+1, nums1, nums2)
                
                #case2
                ans2 = helper(i+1, j , nums1, nums2)
                
                #case3
                ans3 = helper(i , j+1, nums1, nums2)
                
                #case4
                ans4 = nums1[i]*nums2[j]
                
                dp[(i, j)] = max(ans1, ans2, ans3, ans4)
            
                return dp[(i , j)]
            
            return -10**6
                                
        return helper(0,0, nums1, nums2)