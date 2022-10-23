# Problem Link : https://leetcode.com/problems/intersection-of-two-arrays/


from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Empty list to store the answer
        res = []
        # Checking each element in nums1
        for i in nums1:
            # Checking if element is also present in num2
            if i in nums2:
                # Storing common elements in res
                res.append(i)
        return list(set(res))