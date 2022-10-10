## https://leetcode.com/problems/break-a-palindrome/
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p=list(palindrome)
        n=len(p)
        if n==1:return ""
        for i in range(n):
            if p[i]!='a':
                p[i]='a'
                break
        if p!=p[::-1] :
            return "".join(p)
        p=list(palindrome)
        for i in range(n-1,-1,-1):
            if p[i]=='a':
                p[i]='b'
                break
        return "".join(p)
    
