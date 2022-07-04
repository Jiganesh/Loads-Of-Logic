# https://leetcode.com/problems/decode-the-message/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        c = 97
        d = {}
        for i in key:
            if i not in d and  i.isalpha():
                d[i]= chr(c)
                c+=1
               
        return "".join([d[i] if i.isalpha() else " " for i in message])
        
        
    