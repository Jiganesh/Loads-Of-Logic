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