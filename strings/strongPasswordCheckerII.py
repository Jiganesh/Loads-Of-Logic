# https://leetcode.com/problems/strong-password-checker-ii/

class Solution:
    
    # Runtime: 40 ms, faster than 80.00% of Python3 online submissions for Strong Password Checker II.
    # Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Strong Password Checker II.
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        
        if len(password) < 8 : return False
        lower = upper = digit = special = False
        adjacent = True
        
        for index, i in enumerate(password):
            
            if i.islower(): lower=True
            if i.isupper(): upper=True
            if i.isnumeric(): digit=True
            if i in "!@#$%^&*()-+" : special = True
            if index>0 and password[index-1]==password[index]: adjacent = False
                
        return lower and upper and digit and special and adjacent
        