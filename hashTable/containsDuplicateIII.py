# https://leetcode.com/problems/contains-duplicate-iii/
# https://www.youtube.com/watch?v=klCY3k70A50

from sortedcontainers import SortedList

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if abs(nums[i]-nums[j]) <= t and abs(i-j)<=k: 
                    return True
        return False
    

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        container = SortedList()
                
        for index, num in enumerate(nums):
            
            if index>k: container.remove(nums[index-k-1])
            
            left = container.bisect_left(num-t)
            right = container.bisect_right(num+t)
            
            if left != right:
                return True
            
            container.add(num)
            
print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))