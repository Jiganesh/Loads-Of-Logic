# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


from itertools import Counter
class Solution:
    
    # Runtime: 121 ms, faster than 97.86% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
    # Memory Usage: 14.8 MB, less than 93.89% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
    def minDeletions(self, s: str) -> int:

        dictionary = Counter(s)
        
        frequency_chart = set()
        
        deletions = 0
        for _ , value in dictionary.items():
            
            while value>0 and value in frequency_chart:
                deletions+=1
                value-=1
            
            frequency_chart.add(value)
        
        return deletions
                