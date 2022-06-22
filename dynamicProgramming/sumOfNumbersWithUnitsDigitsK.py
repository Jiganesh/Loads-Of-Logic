# https://www.youtube.com/watch?v=LiYMFscvlKU&t=320s
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/discuss/2168461/Python-or-Math-or-Explained

class Solution:
    
    # coin change like solution
    
    # Runtime: 1706 ms, faster than 8.48% of Python3 online submissions for Sum of Numbers With Units Digit K.
    # Memory Usage: 14.1 MB, less than 14.76% of Python3 online submissions for Sum of Numbers With Units Digit K        

    def minimumNumbers(self, num: int, k: int) -> int:
        possible_numbers = [k+ i*10 for i in range (num//10+1)]
        
        dp = [float("inf")]*(num+1)
        dp[0] = 0
        
        for i in possible_numbers:
            for j in range (1, num+1):
                if i<=j:
                    dp[j] = min(1+dp[j-i], dp[j])
                    
        return dp[num] if dp[num] != float('inf') else -1 
    
    
    # Runtime: 34 ms, faster than 93.67% of Python3 online submissions for Sum of Numbers With Units Digit K.
    # Memory Usage: 13.9 MB, less than 74.35% of Python3 online submissions for Sum of Numbers With Units Digit K.
    def minimumNumbers(self, num: int, k: int) -> int:
        
        
        if num == 0:
            return 0
        
        if k == 0:
            return 1 if num % 10 == 0 else -1
        
        for n in range(1, min(num // k, 10) + 1):
            if (num - n * k) % 10 == 0:
                return n
        
        return -1
