# https://leetcode.com/problems/categorize-box-according-to-criteria/

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        bulky = ""
        if (length >= 10**4  or width >= 10**4 or height >= 10**4)  or length * width * height >= 10**9:
            bulky = "Bulky"
        
        heavy = ""
        if mass >= 100:
            heavy = "Heavy"
            
        result = "Neither"
        if bulky and heavy :
            result = "Both"
            return result
        
        if bulky and not heavy:
            return bulky
        elif heavy and not bulky:
            return heavy
        
        return result
            
