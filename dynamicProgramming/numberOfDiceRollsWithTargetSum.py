# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        MOD = 10**9 + 7
        def helper(dice_left, target):
            
            
            if dice_left==0 and target==0:
                return 1
            
            if (dice_left, target) in dp:
                return dp[(dice_left, target)]

            ans = 0
            if dice_left>0 :
                for i in range(1, k+1):
                    ans += helper(dice_left-1, target-i)
            ans = ans % MOD
            
            dp[(dice_left, target)]=ans
            return ans


        return helper(n,target)
    