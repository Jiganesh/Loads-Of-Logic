# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:

    # TC : O(N)
    # SC : O(N)
    
    def removeDigit(self, number: str, digit: str) -> str:
        
        number = list(number)
        last_occurence = None

        for ind , num in enumerate(number):
            if (num == digit):
                last_occurence = ind
                if ind+1 < len(number) and number[ind+1]>digit:
                    number[ind]=""
                    return "".join(number)

        number[last_occurence]=""
        return "".join(number)