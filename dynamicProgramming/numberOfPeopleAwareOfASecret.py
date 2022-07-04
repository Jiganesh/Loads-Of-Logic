# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

class Solution:    
    
    # Runtime: 63 ms, faster than 94.74% of Python3 online submissions for Number of People Aware of a Secret.
    # Memory Usage: 13.9 MB, less than 73.68% of Python3 online submissions for Number of People Aware of a Secret.
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        MOD  = (10**9) + 7
        
        # The dp array will hold number of people know about secret on i th day
        dp = [0] * (n+1)
        
        
        
        dp[1] = 1 # On day one only one person will know
        
        number_of_people_who_know_secret = 1 # 1 till day 1
        
        for i in range (2, len(dp)):
             
            number_of_people_who_can_share_secret =  dp[ max(i-delay,  0) ] 
            number_of_people_who_forgot_secret = dp [ max(i-forget, 0 )  ]
            
            number_of_people_who_know_secret =  number_of_people_who_know_secret - number_of_people_who_forgot_secret+ number_of_people_who_can_share_secret
            dp [i] = number_of_people_who_know_secret % MOD
            
        
        # dp[n+1]  will have number of people who know the secret on last_day. But we have to take out people who will forget secret on last day
        return (dp[-1] - dp[n - forget]) % MOD
            
        
        
        
        
        
        