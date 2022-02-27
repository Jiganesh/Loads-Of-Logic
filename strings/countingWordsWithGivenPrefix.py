class Solution(object):
    
    # Submitted by Jiganesh
    
    # TC: O(N*M)
    # SC : O(N)
    
    # Runtime: 33 ms, faster than 50.00% of Python online submissions for Counting Words With a Given Prefix.
    # Memory Usage: 13.5 MB, less than 100.00% of Python online submissions for Counting Words With a Given Prefix.
    
    # one liner Solution
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        return len( [ i for i in words if i.startswith(pref)])
    
print(Solution().prefixCount(["pay","attention","practice","attend"],"at"))
print(Solution().prefixCount(["pay","lecture","pen","leetcode","codearena"],"code"))