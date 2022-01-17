# https://leetcode.com/problems/word-pattern/
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        # Runtime: 16 ms, faster than 81.24% of Python online submissions for Word Pattern.
        # Memory Usage: 13.4 MB, less than 92.85% of Python online submissions for Word Pattern.
        dictionary = {}
        listOfString = s.split()
        
        if len(listOfString) != len(pattern) or len(set(listOfString)) != len(set(pattern)) :
            return False
            
        for i in range(len(pattern)):
            if pattern[i] in dictionary :
                if dictionary[pattern[i]] != listOfString[i]: return False
            else:
                dictionary[pattern[i]]= listOfString[i]
        return True
    
print(Solution().wordPattern("abba", "dog cat cat dog"))
print(Solution().wordPattern("abba", "dog cat cat fish"))
print(Solution().wordPattern("aaaa", "dog cat cat dog"))
print(Solution().wordPattern("abba", "dog dog dog dog"))
print(Solution().wordPattern("aaaa", "dog dog dog dog"))
print(Solution().wordPattern("aba","cat cat cat dog"))

        
'''
TestCases:

"abba"
"dog cat cat dog"
"abba"
"dog cat cat fish"
"aaaa"
"dog cat cat dog"
"aaaaa"
"cat cat cat cat cat"
"abba"
"dog dog dog dog" 
"aba"
"cat cat cat dog"
'''