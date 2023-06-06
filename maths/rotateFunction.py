# https://leetcode.com/problems/rotate-function/
# https://www.youtube.com/watch?v=mUR13VBC8EQ

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        # F[pivot] = F[0] + sum(array) - len(nums) * array[pivot]
        F0 = 0

        N = len(nums)

        for multiplier, num in enumerate(nums):
            F0 += multiplier * num

        summation = sum(nums)

        result = F0
        Fcurrent = F0

        for i in range(N-1, -1, -1):
            Fcurrent = Fcurrent + summation  - (N * nums[i])
            result = max(Fcurrent, result)

        return result

        
