# https://leetcode.com/problems/unique-binary-search-trees/

class Solution(object):
    def numTrees(self, n):

        """
        :type n: int
        :rtype: int
        """
        
        dp = [1] * (n+1)

        for node in range (2, n+1):
            total = 0
            for root in range (1, node+1):
                left = root-1
                right = node - root
                total += dp[left]*dp[right]
            dp[node]=total

        return dp[n]
