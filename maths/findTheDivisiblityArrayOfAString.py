# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:

        current_num = 0
        result = [0] * len(word)
        for ind, num in enumerate(word) :

            current_num = current_num * 10 + ord(num)-48
            if current_num % m == 0:
                result[ind] = 1

            # Important
            current_num %= m

        return result
