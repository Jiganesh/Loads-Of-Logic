# https://leetcode.com/problems/merge-sorted-array/
# Solution : https://www.youtube.com/watch?v=C4oBXLr3zos

class Solution(object):
    
    # TC : O(N)
    # SC : O(1)
    
    # Runtime: 20 ms, faster than 93.44% of Python online submissions for Merge Sorted Array.
    # Memory Usage: 13.4 MB, less than 46.93% of Python online submissions for Merge Sorted Array.
    
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        pointer1 , pointer2 , i = m-1 , n-1, m+n-1;
        
        while pointer2>=0:
            if pointer1>=0 and nums1[pointer1]> nums2[pointer2]:
                nums1[i]=nums1[pointer1];
                i-=1;
                pointer1-=1
            else :
                nums1[i]=nums2[pointer2]
                i-=1
                pointer2-=1