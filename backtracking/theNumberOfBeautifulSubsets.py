# https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        self.count = 0
        n = len(nums)

        def helper(index, lookup):
            
            if index == n:
                self.count +=1
                return

            if nums[index]+k not in lookup and nums[index]-k not in lookup:
                lookup[nums[index]]+=1
                helper(index+1, lookup)
                lookup[nums[index]]-=1
                if lookup[nums[index]] == 0:
                    del lookup[nums[index]]

            helper(index+1, lookup)

        helper(0, defaultdict(int))
        return self.count-1 # -1 because of empty subset
