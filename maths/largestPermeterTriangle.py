# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    
    # TC : O(NlogN)
    # SC : O(1)
    def largestPerimeter(self, nums) -> int:

        nums.sort()
        n = len(nums)

        result_perimeter = 0
        for ind in range (n-2):
            a = nums[ind]
            b = nums[ind+1]
            c = nums[ind+2]

            if a + b > c :
                result_perimeter = max(result_perimeter, a+b+c)

        return result_perimeter
