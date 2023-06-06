# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        n = len(piles)-1
        self.dp = [[None] * (k+1) for i in range(n+1)]

        def knapsack (i, k):

            if i < 0 or k ==0:
                return 0

            if self.dp[i][k]:
                return self.dp[i][k]
                
            picks = min(len(piles[i]), k)
            exclude = knapsack (i-1, k)

            include, pick_in_pile = 0, 0
            for j in range (picks):
                pick_in_pile += piles[i][j]
                include = max(include, pick_in_pile + knapsack (i-1, k-j-1))

            ans = max( include, exclude)
            self.dp[i][k] = ans
            return ans 

        
        return knapsack( n, k)
        


        