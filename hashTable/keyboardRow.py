# https://leetcode.com/problems/keyboard-row/

class Solution:
    # Runtime: 45 ms, faster than 44.26% of Python3 online submissions for Keyboard Row.
    # Memory Usage: 13.9 MB, less than 16.80% of Python3 online submissions for Keyboard Row.
    def findWords(self, words) :
        dictionary={}
        for index, word in enumerate(["qwertyuiop","asdfghjkl", "zxcvbnm"]):
            for j in word:
                dictionary[j]=index
                
        result =[]
        for i in words:
            word = i
            i = i.lower()
            row = dictionary[i[0]]
            for j in i:
                if dictionary[j]!=row:
                    break
            else: 
                result.append(word)
            
        return result
            
                
        