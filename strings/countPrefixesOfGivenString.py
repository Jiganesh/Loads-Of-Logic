class Solution:
    
    # Runtime: 88 ms, faster than 12.50% of Python3 online submissions for Count Prefixes of a Given String.
    # Memory Usage: 14.1 MB, less than 50.00% of Python3 online submissions for Count Prefixes of a Given String.
    def countPrefixes(self, words, s: str) -> int:
        
        return len([i for i in words if s.startswith(i)])