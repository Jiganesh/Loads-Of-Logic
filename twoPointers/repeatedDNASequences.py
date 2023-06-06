# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        lookup = defaultdict(int)
        n  = len(s)

        result = []
        for ind in range (n-10+1):
            ten_letter_long_seq = s[ind:ind+10]
            lookup[ten_letter_long_seq]+=1

        for key, value in lookup.items():
            if value > 1:
                result.append(key)

        return result