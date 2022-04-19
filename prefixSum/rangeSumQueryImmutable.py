# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):
    
    # Runtime: 81 ms, faster than 70.94% of Python online submissions for Range Sum Query - Immutable.
    # Memory Usage: 17.2 MB, less than 52.30% of Python online submissions for Range Sum Query - Immutable.

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
    
        self.lookupArray =[0]*(len(nums)+1)
        
        for i in range(len(nums)):
            self.lookupArray[i+1] = self.lookupArray[i]+nums[i]

        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.lookupArray[right+1]-self.lookupArray[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)