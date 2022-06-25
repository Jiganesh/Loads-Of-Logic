# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


from itertools import Counter
class Solution:
    
    # Runtime: 179 ms, faster than 73.38% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
    # Memory Usage: 14.8 MB, less than 52.51% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
    def minDeletions(self, s: str) -> int:

        dictionary = Counter(s)
        
        unique = set()
        deletions = 0
        
        for _, val in dictionary.items():
            while val in unique and val :
                val-=1
                deletions+=1
            unique.add(val)
                
        
        return deletions
                