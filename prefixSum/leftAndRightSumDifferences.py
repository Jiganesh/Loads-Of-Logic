# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:

        n = len(nums)
        s = sum(nums)

        current_leftSum = 0
        result = []
        for i in range (1, n+1):
            previous_leftSum = current_leftSum
            current_leftSum = current_leftSum+nums[i-1]
            current_rightSum = s-current_leftSum
            result.append(abs(previous_leftSum - current_rightSum))

        return result