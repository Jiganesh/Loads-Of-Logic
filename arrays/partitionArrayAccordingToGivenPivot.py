class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        return [i for i in nums if i<pivot]+[i for i in nums if i== pivot]+[i for i in nums if i> pivot]
    