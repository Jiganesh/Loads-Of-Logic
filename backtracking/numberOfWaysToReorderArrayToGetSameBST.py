# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 +7
        def helper(nums):
            if not nums: return 1
            root = nums[0]
            left = []
            right = []
            n = len(nums)
            

            for ind in range(1,n):
                if nums[ind] > root:
                    right.append(nums[ind])
                else:
                    left.append(nums[ind])

            return (math.comb(n-1, len(left)) * helper(left) * helper(right) ) % MOD

        return helper(nums)-1

