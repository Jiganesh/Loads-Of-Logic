# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        def sum_of_all_digits(n):
            summation = 0
            while n :
                summation += n%10
                n//=10
            return summation
        

        num_copy = n
        summation_digits = sum_of_all_digits(n)
        i = 0

        while sum_of_all_digits(n) > target:
            
            last_digit = n%10
            n = n//10 + 1
            i+=1       
           
        return n * (10**i) - num_copy
