class Solution(object):
    def findUnsortedSubarray(self, nums):
        if len(nums) <2:
            return 0
        
        prev = nums[0]
        end = 0
		# find the largest index not in place
        for i in range(0, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        start = len(nums) - 1
        prev = nums[start]
		# find the smallest index not in place
        for i in range(len(nums)-1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        if end != 0:
            return end - start + 1
        else: 
            return 0
        
print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))