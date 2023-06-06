# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:


        ps = [0] + list(accumulate(nums, operator.add))
        
        n = len(ps)

        result = []

        for i in range (1,len(ps)):
            left = ps[i-1]
            right = ps[-1] - ps[i]

            numbers_on_left = i-1
            numbers_on_right = n-i-1

            num = nums[i-1]

            abs_diff_left = abs(left - numbers_on_left * num)  
            abs_diff_right = abs(right - numbers_on_right * num)

            total_abs_diff = abs_diff_left + abs_diff_right

            result.append(total_abs_diff)

        return result
