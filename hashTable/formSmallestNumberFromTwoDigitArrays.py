class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

        c = set(nums1)&set(nums2)
        if c:
            return min(c) 
        else:
            a = min(nums1)
            b = min(nums2)
            return min(a, b)*10 + max(a, b)
