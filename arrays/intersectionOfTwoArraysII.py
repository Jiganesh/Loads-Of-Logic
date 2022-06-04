from collections import Counter

class Solution:
    
    # Runtime: 49 ms, faster than 88.96% of Python3 online submissions for Intersection of Two Arrays II.
    # Memory Usage: 14 MB, less than 84.46% of Python3 online submissions for Intersection of Two Arrays II.
    def intersect(self, nums1, nums2):
        
        na = Counter(nums1)
        nb = Counter(nums2)
        
        result  = []
        
        for i in nb:
            if i in na:
                result +=[i]*min(na[i], nb[i])
                
        return result
                