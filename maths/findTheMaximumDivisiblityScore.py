# https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        current_score = 0
        value = float("inf")
        for d in divisors:
            score = 0
            for num in nums:
                score += (num%d == 0)
            
            if score > current_score:
                current_score = score
                value = d
            elif score == current_score:
                value = min(d, value)

        return value