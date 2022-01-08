# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

import collections
class Solution(object):

    #GivesCorrectPalindromicString but TLE
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def palindrome (i, j):
            return i==j[::-1]

        def palindromeword (i):
            return i==i[::-1]

        def makeString(same, two):
            string =""
            start = 0;
            end = len(same)-1

            string = sorted(two, key=len)[-1] if len(two)>0 else ""
            while start <end:
                string = same[start]+string+same[end]
                start+=1;
                end-=1;
            return string

        same = []
        two = []

        for i in range(len(words)):

            for j in range(1,len(words)):
                if i !=j and words[i] and words[j] and palindrome(words[i], words[j]):
                    same = [words[i]]+same+[words[j]]
                    words[i]=""
                    words[j]=""
            if words[i] and palindromeword (words[i]):
                    two.append(words[i])
                    words[i]=""

        return len(makeString(same , two))

    # Instead Of Making String count length of each word and add them still TLE
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def palindrome (i, j):
            return i==j[::-1]

        def palindromeword (i):
            return i==i[::-1]

        same = 0
        maximumTwo=0
        for i in range(len(words)):

            for j in range(1,len(words)):
                if i !=j and words[i] and words[j] and palindrome(words[i], words[j]):
                    same +=2*2
                    words[i]=""
                    words[j]=""
            if words[i] and palindromeword (words[i]):
                    maximumTwo = max(len(words[i]), maximumTwo)
                    words[i]=""

        return same+maximumTwo

    # optimized solution

    # 2 Key Points:
    #     the center word can only contain only two identical letters like 'aa'
    #         for example 'bcaacb'
    #         palindrome may not contain center word, for example 'bccb'
    #     only pairs like ('aa', 'aa') or ('ab', 'ba') can put on two sides respectively
    #         so we count the 'aa' and 'abba' patterns
    #         if the count of 'aa' pattern is odd, the left one can be the center word
    def longestPalindrome(self, words):
        wc = collections.Counter(words)
        aa = 0  # count how many words contain only two identical letters like 'aa'
        center = 0  # if one count of 'aa' is odd, that means it can be the center of the palindrome, answer can plus 2
        abba = 0 # count how many word pairs like ('ab', 'ba') and they can put on both sides respectively

        for w, c in wc.items():
            if w[0] == w[1]: # like 'aa', 'bb', ...
                aa += c // 2 * 2 # if there are 3 'aa', we can only use 2 'aa' put on both sides respectively
                # if one count of 'aa' is odd, that means it can be the center of the palindrome, answer can plus 2
                if c % 2 == 1: center = 2
            else:
                abba += min(wc[w], wc[w[::-1]]) * 0.5  # will definitely double counting
        return aa * 2 + int(abba) * 4 + center


print(Solution().longestPalindrome((["lc","cl","gg"]))) # 6
print(Solution().longestPalindrome((["ab","ty","yt","lc","cl","ab"]))) # 8
print(Solution().longestPalindrome((["cc","ll","xx"]))) #2
print(Solution().longestPalindrome(["gg","gg"])) #4
print(Solution().longestPalindrome(["gg","gg", "gg"])) #6
print(Solution().longestPalindrome(["gg"])) #2
print(Solution().longestPalindrome(["gl"])) #0


