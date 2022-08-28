# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    
    # Runtime: 236 ms, faster than 14.29% of Python3 online submissions for Removing Stars From a String.
    # Memory Usage: 15.7 MB, less than 14.29% of Python3 online submissions for Removing Stars From a String.
    
    def removeStars(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch == "*" :
                stack.pop()
                continue
            stack.append(ch)
            
        return "".join(stack)