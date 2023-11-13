# https://leetcode.com/problems/sort-vowels-in-a-string/
class Solution:
    # TC : O(N) + O(klogk) where N - length of string and k is number of vowels
    # SC : O(N) where N length of string - Used List to replace chr as strings manipulation is computationally expensive

    def sortVowels(self, s: str) -> str:

        vowels  = "AEIOUaeiou"
        vowels_in_s = [i for i in s if i in vowels]

        vowels_in_s.sort(reverse=True)
        
        result = list(s)

        for index, ch in enumerate(result):
            if ch in vowels:
                result[index] = vowels_in_s.pop()

        return "".join(result)
