# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution:
    def punishmentNumber(self, n: int) -> int:

        def possible(sum_till_now, possible_number, remaining_string, target):

            if not remaining_string:
                return (sum_till_now + possible_number) == target

            digit = int(remaining_string[0])
            
            # Two choices:

            # 1. Add the number as a sum
            # 2. Add other numbers to the number

            case1 = possible(sum_till_now + possible_number, digit, remaining_string[1:], target) 
            case2 = possible(sum_till_now, possible_number*10 + digit, remaining_string[1:], target)

            return case1 or case2

        result = 0


        for i in range (1, n+1):
            if possible(0, 0, str(i*i), i):
                result += (i*i)

        return result
