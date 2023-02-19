# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        lookup = defaultdict(int)
        for u, v in nums1:
            lookup[u]+=v
        for u, v in nums2:
            lookup[u]+=v
            
        a = [[key, value] for key, value in lookup.items()]
        return sorted(a)