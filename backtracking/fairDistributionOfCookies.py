# https://leetcode.com/problems/fair-distribution-of-cookies/submissions/

class Solution:
    # Runtime: 65 ms, faster than 100.00% of Python3 online submissions for Fair Distribution of Cookies.
    # Memory Usage: 14 MB, less than 37.50% of Python3 online submissions for Fair Distribution of Cookies.
    def distributeCookies(self, cookies, k: int) -> int:
        
        n = len(cookies)
        self.minimum_unfairness = float('inf')
        
        def backtracking (cookies, k, index, n, result):
            
            if index == n:
                maximum_total = max(result)
                self.minimum_unfairness = min(self.minimum_unfairness, maximum_total)
                return
            
            # TLE if below optimization not done
            # This optimization reduces unnecessary backtracking
            if self.minimum_unfairness <= max(result):
                return 
                
            for i in range (k):
                result[i] += cookies[index]
                backtracking(cookies, k , index+1, n , result )
                result[i] -= cookies[index]
        
        backtracking (cookies, k, 0, n , [0]*k)
        return self.minimum_unfairness
        
        
                
print(Solution().distributeCookies([76265,7826,16834,63341,68901,58882,50651,75609], 8))