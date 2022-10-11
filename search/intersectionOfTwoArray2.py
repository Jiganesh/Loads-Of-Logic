# Problem Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/


from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         In this problem, We have to return the array with minimum occurances of the element in both the array
    
#     We have created Counter or frequency hashmap to count the elements with their occurances. 
    
#     We will traverse any one of the hashmap and insert the element min times of the both occurances. 
    
#     for eg: if element 1 occurs 5 times in nums1 and 2 times in nums2, 
#         the resultant array would have element 1 only 2 times. 
    
        a = Counter(nums1)
        b = Counter(nums2)
        
        res = []
        for i in a:
            if i in nums2:
                temp = [i] * min(a[i],b[i])
                res += temp
        return res