# https://leetcode.com/problems/median-of-two-sorted-arrays/

# https://www.youtube.com/watch?v=NTop3VTjmxk
from typing import List
class Solution:
    
    # Naive Approach
    
    # TC : O(NlogN)
    # SC : O(N)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = nums1+nums2
        nums.sort()
        l = len(nums)
        if l%2==0:
            mid = l//2
            res=(nums[mid-1]+nums[mid])/2
        else:
            res = nums[l//2]

        return res


    # TC : O(log min(N1, N2))
    # SC : O(1)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        

        n1 = len(nums1)
        n2 = len(nums2)

        if n2 < n1 :
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0 
        high = n1

        res = 0

        while low <= high:
            
            print("inside")
            cut1 = (low+high)//2
            cut2 = (n1+n2+1)//2 - cut1

            left1 = float("-inf") if cut1 == 0 else nums1[cut1-1]
            left2 = float("-inf") if cut2 == 0 else nums2[cut2-1]

            right1 = float("inf") if cut1 == n1 else nums1[cut1]
            right2 = float("inf") if cut2 == n2 else nums2[cut2]

            print(left1, left2, right1, right2)

            if left1 <= right2 and left2 <= right1:

                if (n1+n2)%2==0:
                    
                    return (max(left1, left2) + min(right1, right2))/2
                else:
                    return max(left1, left2)

            elif left1 > right2:
                high = cut1-1
            
            else:
                low = cut1+1
