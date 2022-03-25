# https://leetcode.com/problems/target-sum/

class Solution(object):
    
    # Runtime: 188 ms, faster than 83.65% of Python online submissions for Target Sum.
	# Memory Usage: 13.8 MB, less than 62.97% of Python online submissions for Target Sum.
 
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if (sum(nums) + target) % 2 == 1:
            return 0

        sumPartition1 = abs((sum(nums)+target)//2)

        dp = [[0 for i in range (sumPartition1+1)]  for i in range(len(nums)+1)]

        for i in range(len(nums)+1):
            for j in range(sumPartition1+1):
                if j == 0:
                    dp[i][j] = 1

        for i in range(1, len(nums)+1):
            for j in range(sumPartition1+1):
                if nums[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-nums[i-1]])%1000000007
                else:
                    dp[i][j] = (dp[i-1][j])%1000000007

        return dp[len(nums)][sumPartition1]

print(Solution().targetSum(3, [1, 1, 1, 1, 1]))
