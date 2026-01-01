# https://leetcode.com/problems/plus-one/

class Solution:
    # TC: O(N)
    # SC: O(N)
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)-1
        add = 1

        while n >= 0:
            addition = digits[n]+ add
            if addition <= 9:
                digits[n] = addition
                return digits
            else:
                digits[n] = addition % 10
                add = addition // 10
            
            n-=1

        return ([add] if add else []) + digits



        
