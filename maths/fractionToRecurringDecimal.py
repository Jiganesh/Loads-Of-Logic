# https://leetcode.com/problems/fraction-to-recurring-decimal/


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:


        # Handle base case if numerator or denominator is zero
        if numerator == 0:
            return "0"
        if denominator == 0:
            return ""

        result = ""
        
        # Handle the case of negatives
        if (numerator < 0) ^ (denominator < 0):
            result += "-"
        numerator, denominator  = abs(numerator) , abs(denominator)


        # add the integer part 
        result += str(numerator//denominator)
        if numerator%denominator == 0:
            return result

        result += "."
        remainder = numerator%denominator

        remainder_dictionary = {} # key as remainder, value as len or result

        while remainder != 0 and remainder not in remainder_dictionary:
            remainder_dictionary[remainder] = len(result)
            remainder*=10
            result+=str(remainder//denominator)
            remainder = remainder%denominator
        
        if remainder:
            length_of_non_repeating_start = remainder_dictionary[remainder]
            start = result[:length_of_non_repeating_start]
            repeated = "(" + result[length_of_non_repeating_start:] + ")"
            return start + repeated

        return result

        
        
