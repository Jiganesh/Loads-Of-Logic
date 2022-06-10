class Solution:
    
    # Runtime: 139 ms, faster than 26.67% of Python3 online submissions for Longest Substring Without Repeating Characters.
    # Memory Usage: 14.1 MB, less than 13.62% of Python3 online submissions for Longest Substring Without Repeating Characters.

    # TC : O(NlogN)
    # SC : O(N)
    
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lookup = set()
        left = result =right =0
        while right < len(s):
            while s[right] in lookup:
                lookup.remove(s[left])
                left+=1
            lookup.add(s[right])
            right+=1
            result = max(result, len(lookup))
            
        return result
        
    # Runtime: 86 ms, faster than 60.14% of Python3 online submissions for Longest Substring Without Repeating Characters.
    # Memory Usage: 14.1 MB, less than 13.62% of Python3 online submissions for Longest Substring Without Repeating Characters.        
     
    # TC : O(N)
    # SC : O(1)   
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dictionary = {}
        result , left , right = 0,0 ,0
        
        while right < len (s):
            character = s[right]
            if character in dictionary :
                left = max( dictionary[character]+1, left)
            dictionary[character]=right
            right+=1
            result = max(result, right-left)

        return result