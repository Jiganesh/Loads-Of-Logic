# https://leetcode.com/problems/calculate-amount-paid-in-taxes/
class Solution:
    # Runtime: 114 ms, faster than 15.38% of Python3 online submissions for Calculate Amount Paid in Taxes.
    # Memory Usage: 13.9 MB, less than 23.08% of Python3 online submissions for Calculate Amount Paid in Taxes.
    def calculateTax(self, brackets, income):
        
        tax = 0
        for index, i in enumerate(brackets):
            u, v = i
            prev_u , prev_v = brackets[index-1] if index>0 else [0,0] 
            if index == 0 and u<= income:
                tax += u*v/100.0
            elif u<=income :
                tax += (u-prev_u)*v/100.0
            elif u > income:
                tax += (income-prev_u)*v /100.0
                break
        return tax
            
            
            